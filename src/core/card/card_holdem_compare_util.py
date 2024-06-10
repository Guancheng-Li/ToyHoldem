"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Help compare 5 cards.
"""

from typing import Dict, List, Tuple

from core.card.card_object import Card, sort_card_by_point
from core.card.card_holdem_type import (
    CardType, card_type_of_5_cards, group_by_point)


def compare_2_group(group_1: List[Card], group_2: List[Card]) -> int:
    group_1_value = card_type_of_5_cards(group_1)
    group_2_value = card_type_of_5_cards(group_2)
    if group_1_value > group_2_value:
        return 1
    elif group_1_value < group_2_value:
        return -1
    return compare_2_group_in_same_type(group_1, group_2, group_1_value)


def compare_2_group_in_same_type(
    group_1: List[Card], group_2: List[Card], card_type: CardType) -> int:
    group_1_sorted = sort_card_by_point(group_1)
    group_1_grouped = group_by_point(group_1_sorted)
    group_2_sorted = sort_card_by_point(group_2)
    group_2_grouped = group_by_point(group_2_sorted)
    if card_type == CardType.ROYAL_FLUSH:
        return 0
    elif card_type == CardType.STRAIGHT_FLUSH:
        return _compare_straight_flush(group_1_sorted, group_2_sorted)
    elif card_type == CardType.FOUR_OF_A_KIND:
        return _compare_four_of_a_kind(group_1_grouped, group_2_grouped)

    return 0


def _compare_straight_flush(group_1: List[Card], group_2: List[Card]) -> int:
    if group_1[0].point() > group_2[0].point():
        return 1
    elif group_1[0].point() < group_2[0].point():
        return -1
    return 0


def _compare_four_of_a_kind(group_1: Dict[int, int], group_2: Dict[int, int]) -> int:
    def _get_duplicated_and_single(group: Dict[int, int]) -> Tuple[int, int]:
        duplicated = None
        single = None
        for key, value in group.items:
            if value == 4:
                duplicated = key
            else:
                single == key
        return duplicated, single
    group_1_duplicated, group_1_single = _get_duplicated_and_single(group_1)
    group_2_duplicated, group_2_single = _get_duplicated_and_single(group_2)
    if group_1_duplicated > group_2_duplicated:
        return 1
    elif group_1_duplicated < group_2_duplicated:
        return -1

    if group_1_single > group_2_single:
        return 1
    elif group_1_single < group_2_single:
        return -1
    return 0


