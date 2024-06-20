"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The state machine of round.
"""

import enum
import random
from typing import List

from core.card.card_holdem_compare_util import compare_2_group
from core.card.card_holdem_selection_util import select_high_score_cards
from core.card.card_object import Card, CardPack
from core.rule.action import Action, ActionType
from core.rule.player import Player, Role
from core.rule.pot import Pot


class RoundState(enum.Enum):
    BEGIN = 0
    PRE_FLOP = 1
    FLOP = 2
    TURN_0 = 3
    TURN_1 = 4
    TURN_2 = 5
    RIVER = 6

class RoundStateMachine:
    def __init__(self, players: List[Player]):
        self._state = RoundState.BEGIN
        self._round_id = 0
        self._players = players
        # Next line: 1st is the dealer or nearest player.
        self._alive_players_from_dealer = []
        self._pot = Pot()
        self._cards = []
        self._shared_cards = []
        self._player_cards = {}
        self._dealer_index = None  # real index
        self._winner_index = None  # real index
        self._winner_card = []

    def _update_state(self):
        """Update the state of round, change round_id etc."""
        self._round_id += 1
        self._state = RoundState(self._round_id)

    def _real_index(self, virtual_index: int) -> int:
        """Tool function to get the real index by virtual_index.
           Note that the index is not player_id.
           The virtual_index 0 is the dealer.
        """
        return (self._dealer_index + virtual_index) % len(self._players)

    def _update_cards(self):
        """Update the shared cards are fold or unfold."""
        # TODO
        return

    def _initialize_players(self):
        """To find out the dealer and set small blind and big blind."""
        player_size = len(self._players)
        for i in range(player_size):
            if self._players[i].role() == Role.DEALER:
                assert self._dealer_index is None
                self._dealer_index = i
                self._players[
                    self._player[self._real_index(i + 1)]].set_small_blind()
                self._players[
                    self._player[self._real_index(i + 2)]].set_big_blind()

    def _initialize_cards(self):
        """Shuffle cards and give out to users."""
        self._cards = CardPack.cards_without_joker()
        random.shuffle(self._cards)
        self._shared_cards = self._cards[:5]
        player_size = len(self._players)
        for i in range(player_size * 2):
            player_index = self._real_index(i)
            self._player_cards[player_index] = self._player_cards.get(
                    player_index, []).append(self._cards[5 + i])

    def _transverse_alive_players_for_bet(self):
        """For each round, ask every player for raise/fold/check."""
        if self._state == RoundState.PRE_FLOP:
            small_blind_action = self._player[self._real_index(1)].action()
            self._update_by_action(small_blind_action)
            big_blind_action = self._player[self._real_index(2)].action()
            self._update_by_action(big_blind_action)
            for i in range(3, len(self._players) + 1):
                player_index = self._real_index(i)
                action = self._players[player_index].action()
                self._update_by_action(action)
            return
        for i in range(1, len(self._players) + 1):
            player_index = self._real_index(i)
            if not self._players[player_index].is_alive():
                continue
            action = self._players[player_index].action()
            self._update_by_action(action)

    def _transverse_alive_players_for_call(self):
        """For each round, ask every player for call."""
        for i in range(1, len(self._players) + 1):
            player_index = self._real_index(i)
            if not self._players[player_index].is_alive():
                continue
            action = self._players[player_index].action()
            self._update_by_action(action, player_index)

    def _update_by_action(self, action: Action, player_index: int):
        """Update the state and pot by action."""
        '''
          Draft:
          timeout = false
          time_start = time.time()
          while(timeout()):
              if time.time() - time_start > 10:
                  timeout = true
                  break
              if self._players[player_index].is_alive():
                  action = player.action()
                  if update_by_action(action, player_index):
                      break
          if timeout:
              run_default_action()
        '''
        assert self._players[player_index].is_alive()
        if action.type() == ActionType.FOLD:
            self._players[player_index].set_fold()
        elif action.type() == ActionType.CALL:
            # TODO: 
            # 0. Check pay possible.
            # 1. CHECK how much need to match.
            # 2. Pay.
            pass
        elif action.type() == ActionType.RAISE:
            # TODO: 
            # 0. Check pay possible.
            # 1. Update the highest score.
            # 2. Pay.
            pass
        elif action.type() == ActionType.CHECK:
            # TODO: The latest one cannot check.
            pass
        elif action.type() == ActionType.BET:
            # TODO:
            # 0. Check pay possible.
            # 1. Pay.
            pass
        elif action.type() == ActionType.ALL_IN:
            # TODO(Guancheng Li): More rule details for implement.
            # 0. Check pay possible.
            # 1. Pay.
            pass

    def _update_alive_players_from_dealer(self):
        """Process the round state by players action."""
        alive_players = []
        for i in range(len(self._players)):
            player_index = self._real_index(i)
            if self._players[player_index].is_alive():
                alive_players.append(player_index)
        self._alive_players_from_dealer = alive_players

    def _is_end(self) -> bool:
        """Check if the round is end."""
        return len(self._alive_players_from_dealer) == 1

    def _river_compare(self):
        """Compare the cards of alive players in river round."""
        alive_player_best_cards = {}
        for i in range(len(self._players)):
            player_index = self._real_index(i)
            if not self._players[player_index].is_alive():
                continue
            alive_player_best_cards[player_index] = select_high_score_cards(
                self._shared_cards + self._player_cards[player_index])
        for i in range(len(self._players)):
            player_index = self._real_index(i)
            if self._winner_index is None:
                self._winner_index = [player_index]
                continue
            res = compare_2_group(
                alive_player_best_cards[self._winner_index],
                alive_player_best_cards[player_index])
            if res == 0:
                self._winner_index.append(player_index)
            elif res == -1:
                self._winner_index = [player_index]
        for index in self._winner_index:
            self._winner_card.append(alive_player_best_cards[index])

    def _update_only_winner(self):
        """Update the winner when the round is not end."""
        self._winner_index = [
            self._real_index(self._alive_players_from_dealer[0])]

    def _update_score(self):
        """Update score for the winners."""
        total_score = self._pot.total_score()
        winner_size = len(self._winner_index)
        peer_score = int(1.0 * total_score / winner_size)
        for index in self._winner_index:
            self._players[index].add_score(peer_score)
        # For the score cannot be divided,
        # give it to the winner nearest to dealer.
        remainder_score = total_score - peer_score * winner_size
        self._players[self._winner_index[0]].add_score(remainder_score)

    def start(self):
        """Start a new game with several rounds."""
        self._initialize_players()
        self._initialize_cards()
        self._update_state()

    def execute(self):
        """The whole game."""
        assert self._state != RoundState.BEGIN
        while not self.is_end() and self._state != RoundState.RIVER:
            self._update_cards()
            self._transverse_alive_players_for_bet()
            self._update_alive_players_from_dealer()
            if self.is_end():
                break
            self._transverse_alive_players_for_call()
            self._update_alive_players_from_dealer()
        if self._state == RoundState.RIVER:
            self._river_compare()
            self._update_score()
        else:
            self._update_only_winner()
            self._update_score()
