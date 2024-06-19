"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The pot of one game.
"""

import enum
from typing import List


class AddType(enum.Enum):
    CALL = 0
    RAISE = 1
    ALL_IN = 2
    BET = 3
    BIG_BLIND_BET = 4
    SMALL_BLIND_BET = 5


class AddItem:
    def __init__(self, player_id: int, amount: int, add_type: AddType, round_id: int):
        self.amount = amount
        self.add_type = add_type
        self.player_id = player_id
        self.round_id = round_id


class Pot:
    def __init__(self):
        self._pre_round_history = []
        self._pre_round_score = 0
        self._current_round_history = []
        self._current_round_score = 0
        self._player_pre_round_history = {}
        self._player_pre_round_score = {}
        self._player_current_round_history = {}
        self._player_current_round_score = {}

    def total_score(self) -> int:
        return self._pre_round_score + self.current_score()

    def current_score(self) -> int:
        return self._sum_score(self._current_round_history)

    def _sum_score(self, history: List[AddItem]) -> int:
        res = 0
        for item in history:
            res += item.amount
        return res

    def add(self, player_id: int, amount: int, add_type: AddType, round_id: int):
        add_item = AddItem(player_id, amount, add_type, round_id)
        self._current_round_history.append(add_item)
        self._current_round_score += amount
        self._player_current_round_history.get(player_id, []).append(add_item)
        self._player_current_round_score = \
            self._player_current_round_score.get(player_id, 0) + amount

    def next_round(self):
        self._pre_round_history += self._current_round_history
        self._pre_round_score += self._current_round_score
        for player_id, action_item in self._player_current_round_history.items():
            self._player_pre_round_history[player_id] = \
                self._player_pre_round_history.get(player_id, []) + action_item
            self._player_pre_round_score[player_id] = \
                self._player_pre_round_score.get(player_id, 0) + \
                    self._player_current_round_score.get(player_id, 0)
        self._reset_current_round()

    def _reset_current_round(self):
        self._current_round_history = []
        self._current_round_score = 0
        self._player_current_round_history = {}
        self._player_current_round_score = {}

    def reset(self):
        self._history = []

    def get_player_history(self, player_id: int, current_round=False) -> List[AddItem]:
        if current_round:
            return self._player_current_round_history.get(player_id, [])
        return self._player_pre_round_history.get(player_id, []) + \
            self._player_current_round_history.get(player_id, [])

    def get_player_score(self, player_id: int, current_round=False) -> int:
        if current_round:
            return self._player_current_round_score.get(player_id, 0)
        return self._player_pre_round_score.get(player_id, 0) + \
            self._player_current_round_score.get(player_id, 0)
