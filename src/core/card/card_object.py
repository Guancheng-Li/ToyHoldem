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
    JOKER = 4


class CardJoker(enum.Enum):
    """The joker of a card, not used but for label."""
    COLOR_JOKER = 14
    BLACK_JOKER = 15


class Card:
    """A card."""
    def __init__(self, color: CardColor, point: int):
        self._color = None
        self._point = None
        if color is not None:
            assert isinstance(color, CardColor)
            self._color = color
        if point is not None:
            assert isinstance(point, int) and point <= 15 and point >= 1
            self._point = point
        if point > 13:
            # For joker, the point equals to CardJoker.Type.value
            assert self._color == CardColor.JOKER
        self._unique_id = uuid.uuid4()

    def color(self) -> CardColor:
        return self._color

    def is_joker(self) -> bool:
        return self.color() == CardColor.JOKER

    def point(self) -> int:
        return self._point

    def joker_type(self) -> Optional[CardJoker]:
        if self.is_joker():
            return CardJoker.COLOR_JOKER \
                if self._point == 14 else CardJoker.BLACK_JOKER
        return None

    def encode(self) -> str:
        return f'{self.color().value}_{self._point}'

    def unique_id(self) -> str:
        return self._unique_id

    @classmethod
    def decode(cls, str):
        tokens = str.split('_')
        assert len(tokens) == 2
        color_value = int(tokens[0])
        assert color_value >= 0 and color_value <= 4
        point = int(tokens[1])
        assert point >= 1 and point <= 15
        return Card(color_value, point)


def CardPack():
    @staticmethod
    def cards_without_joker() -> List[Card]:
        cards = []
        for color in CardColor:
            for point in range(1, 14):
                cards.append(Card(color, point))
        return cards

    @staticmethod
    def cards_origin() -> List[Card]:
        cards = CardPack.cards_without_joker()
        cards.append(Card(CardColor(4), 14))
        cards.append(Card(CardColor(4), 15))
        return cards


def sort_card_by_point(cards: List[Card], descend=False) -> List[Card]:
    joker_group = [card for card in cards if card.is_joker()]
    joker_group.sort(key=lambda e: e.joker_type)
    point_group = [card for card in cards if not card.is_joker()]
    point_group.sort(key=lambda e: e.point())
    if descend:
        return joker_group + reversed(point_group)
    return joker_group + point_group
