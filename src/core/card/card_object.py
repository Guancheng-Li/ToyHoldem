"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Defines the cards.
"""

import enum
from typing import List
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
    def __init__(self, color, point, joker=None):
        if color is not None:
            assert isinstance(color, CardColor)
            self._color = color
        if point is not None:
            assert isinstance(point, int) and point <= 12 and point >= 1
            self._point = point
        if joker is not None:
            assert isinstance(joker, CardJoker)
            self._joker = joker
        self._unique_id = uuid.uuid4()

    def is_joker(self):
        return self._joker is not None

    def color(self):
        if not self.is_joker():
            return self._color
        return None

    def point(self):
        if not self.is_joker():
            return self._point
        return None

    def encode(self) -> str:
        raise NotImplementedError('Not implemented yet.')

    def decode(self) -> str:
        raise NotImplementedError('Not implemented yet.')


def CardPacket():
    @classmethod
    def cards_without_joker(cls) -> List[Card]:
        cards = []
        for color in CardColor:
            for point in range(1, 13):
                cards.append(Card(color, point))
        return cards

    @classmethod
    def cards_origin(cls) -> List[Card]:
        cards = CardPacket.cards_without_joker()
        cards.append(Card(None, None, CardJoker.COLOR_JOKER))
        cards.append(Card(None, None, CardJoker.BLACK_JOKER))
        return cards

