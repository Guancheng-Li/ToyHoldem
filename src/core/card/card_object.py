"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Defines the cards.
"""

import enum
from typing import List, Optional
import uuid


class CardColor(enum.Enum):
    """The color of a card."""
    HEART = 0
    SPADE = 1
    CLUB = 2
    DIAMOND = 3


class CardJoker(enum.Enum):
    """The joker of a card."""
    COLOR_JOKER = 0
    BLACK_JOKER = 1


class Card:
    """A card."""
    def __init__(self, color: CardColor, point: int, joker=None):
        self._color = None
        self._point = None
        self._joker = None
        if color is not None:
            assert isinstance(color, CardColor)
            self._color = color
        if point is not None:
            assert isinstance(point, int) and point <= 13 and point >= 1
            self._point = point
        if joker is not None:
            assert isinstance(joker, CardJoker)
            self._joker = joker
        self._unique_id = uuid.uuid4()

    def is_joker(self) -> bool:
        return self._joker is not None

    def color(self) -> Optional[CardColor]:
        if not self.is_joker():
            return self._color
        return None

    def point(self) -> Optional[int]:
        if not self.is_joker():
            return self._point
        return None

    def joker_type(self) -> Optional[CardJoker]:
        if self.is_joker:
            return self._joker
        return None

    def encode(self) -> str:
        raise NotImplementedError('Not implemented yet.')

    def decode(self) -> str:
        raise NotImplementedError('Not implemented yet.')


def CardPack():
    @classmethod
    def cards_without_joker(cls) -> List[Card]:
        cards = []
        for color in CardColor:
            for point in range(1, 14):
                cards.append(Card(color, point))
        return cards

    @classmethod
    def cards_origin(cls) -> List[Card]:
        cards = CardPack.cards_without_joker()
        cards.append(Card(None, None, CardJoker.COLOR_JOKER))
        cards.append(Card(None, None, CardJoker.BLACK_JOKER))
        return cards


def sort_card_by_point(cards: List[Card], descend=False) -> List[Card]:
    joker_group = [card for card in cards if card.is_joker()]
    joker_group.sort(key=lambda e: e.joker_type)
    point_group = [card for card in cards if not card.is_joker()]
    point_group.sort(key=lambda e: e.point())
    if descend:
        return joker_group + reversed(point_group)
    return joker_group + point_group
