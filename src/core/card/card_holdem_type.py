"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Defines card type of 5 cards.
"""

import enum
from typing import Dict, List

from core.card.card_object import Card, sort_card_by_point


class CardType(enum.Enum):
    """The type of a card."""
    HIGH_CARD = 0  # 高牌
    ONE_PAIR = 1  # 一对
    TWO_PAIR = 2  # 两对
    THREE_OF_A_KIND = 3  # 三条
    STRAIGHT = 4  # 顺子
    FLUSH = 5  # 同花
    FULL_HOUSE = 6  # 葫芦（三条带一对）
    FOUR_OF_A_KIND= 7  # 四条（金刚）
    STRAIGHT_FLUSH = 8  # 同花顺
    ROYAL_FLUSH = 9  # 皇家同花顺


def card_type_of_5_cards(cards: List[Card]) -> CardType:
    """Judge type of 5 cards."""
    assert len(cards) == 5, 'Cannot judge cards type with cards num not equal to 5'
    cards = sort_card_by_point(cards)
    card_point_cnt = group_by_point(cards)
    if _is_royal_flush(cards):
        return CardType.ROYAL_FLUSH
    elif _is_straight_basic(cards):
        return CardType.STRAIGHT_FLUSH
    elif _is_four_of_a_kind(card_point_cnt):
        return CardType.FOUR_OF_A_KIND
    elif _is_full_house(card_point_cnt):
        return CardType.FULL_HOUSE
    elif _is_flush_basic(cards):
        return CardType.FLUSH
    elif _is_straight_basic(cards):
        return CardType.STRAIGHT
    elif _is_three_of_a_kind(card_point_cnt):
        return CardType.THREE_OF_A_KIND
    elif _is_two_pair(card_point_cnt):
        return CardType.TWO_PAIR
    elif _is_one_pair(card_point_cnt):
        return CardType.ONE_PAIR
    return CardType.HIGH_CARD


def _is_royal_flush(cards: List[Card]) -> bool:
    """Test if cards are royal flush."""
    return _is_straight_flush_basic(cards) and cards[0].point() == 10


def _is_straight_flush_basic(cards: List[Card]) -> bool:
    """Only test if cards are straight flush but not judge higher level."""
    return _is_flush_basic(cards) and _is_straight_basic(cards)


def _is_four_of_a_kind(card_point_cnt: Dict[int, int]) -> bool:
    """Test if cards are four of a kind."""
    if len(list(card_point_cnt.keys())) != 2:
        return False
    return max(list(card_point_cnt.values())) == 4


def _is_full_house(card_point_cnt: Dict[int, int]) -> bool:
    """Test if cards are full house."""
    if len(list(card_point_cnt.keys())) != 2:
        return False
    return max(list(card_point_cnt.values())) == 3


def _is_flush_basic(cards: List[Card]) -> bool:
    """Only test if cards are flush but not judge higher level."""
    color = None
    for item in cards:
        if color is None:
            color = item.color()
        elif color != item.color():
            return False
    return True


def _is_straight_basic(cards: List[Card]) -> bool:
    """Only test if cards are straight but not judge higher level."""
    min_point = None
    for idx, item in enumerate(cards):
        if min_point is None:
            min_point = item.point()
        elif item.point() != (idx + min_point()) % 13:
            return False
    return min_point <= 10


def _is_three_of_a_kind(card_point_cnt: Dict[int, int]) -> bool:
    """Test if cards are three of a kind."""
    if len(list(card_point_cnt.keys())) != 3:
        return False
    return max(list(card_point_cnt.values())) == 3


def _is_two_pair(card_point_cnt: Dict[int, int]) -> bool:
    """Test if cards are two pair."""
    if len(list(card_point_cnt.keys())) != 3:
        return False
    return max(list(card_point_cnt.values())) == 2


def _is_one_pair(card_point_cnt: Dict[int, int]) -> bool:
    """Test if cards are one pair."""
    return len(list(card_point_cnt.keys())) == 4


def group_by_point(cards: List[Card]) -> Dict[int, int]:
    """Group cards point and count."""
    result = {}
    for item in cards:
        result[item.point()] = result.get(item.point(), 0) + 1
    return result
