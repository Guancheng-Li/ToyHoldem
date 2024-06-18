"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Help compare 5 cards.
"""

from typing import Dict, List, Tuple

from core.card.card_object import Card, sort_card_by_point
from core.card.card_holdem_type import (
    CardType, card_type_of_5_cards, group_by_point)


def compare_2_group(group_1: List[Card], group_2: List[Card]) -> int:
    group_1_type = card_type_of_5_cards(group_1)
    group_2_type = card_type_of_5_cards(group_2)
    if group_1_type != group_2_type:
        return compare_2_diff_type(group_1_type, group_2_type)
    return compare_2_group_in_same_type(group_1, group_2, group_1_type.value)


def compare_2_diff_type(type_1: CardType, type_2: CardType):
    assert type_1 != type_2
    return 1 if type_1.value > type_2.value else -1


def compare_2_group_in_same_type(
    cards_1: List[Card], cards_2: List[Card], card_type: CardType) -> int:
    cards_1_sorted = sort_card_by_point(cards_1)
    cards_1_grouped = group_by_point(cards_1_sorted)
    cards_2_sorted = sort_card_by_point(cards_2)
    cards_2_grouped = group_by_point(cards_2_sorted)
    if card_type == CardType.ROYAL_FLUSH:
        return 0  # Only 1 royal flush could exist.
    elif card_type == CardType.STRAIGHT_FLUSH:
        # All colors are equal.
        return _compare_straight(cards_1_sorted, cards_2_sorted)
    elif card_type == CardType.FOUR_OF_A_KIND:
        return _compare_with_priority(cards_1_grouped, cards_2_grouped, 4)
    elif card_type == CardType.FULL_HOUSE:
        return _compare_with_priority(cards_1_grouped, cards_2_grouped, 3)
    elif card_type == CardType.FLUSH:
        return _compare_reversed_points(cards_1_sorted, cards_2_sorted)
    elif card_type == CardType.STRAIGHT:
        return _compare_straight(cards_1_sorted, cards_2_sorted)
    elif card_type == CardType.THREE_OF_A_KIND:
        return _compare_with_priority(cards_1_grouped, cards_2_grouped, 3)
    elif card_type == CardType.TWO_PAIR:
        return _compare_with_priority(cards_1_grouped, cards_2_grouped, 2)
    elif card_type == CardType.ONE_PAIR:
        return _compare_with_priority(cards_1_grouped, cards_2_grouped, 2)
    elif card_type == CardType.HIGH_CARD:
        return _compare_reversed_points(cards_1_sorted, cards_2_sorted)
    return 0  # Impossible to reach here.


def _compare_straight(cards_1_sorted: List[Card], cards_2_sorted: List[Card]) -> int:
    if cards_1_sorted[0].point() != 1 and cards_2_sorted[0].point() != 1:
        if cards_1_sorted[0].point() > cards_2_sorted[0].point():
            return 1
        elif cards_1_sorted[0].point() < cards_2_sorted[0].point():
            return -1
        return 0
    if cards_1_sorted[0].point() == 1 and cards_2_sorted[0].point() != 1:
        if cards_1_sorted[1].point() == 2:
            return -1
        else:
            return 1
    if cards_1_sorted[0].point() != 1 and cards_2_sorted[0].point() == 1:
        if cards_2_sorted[1].point() == 2:
            return 1
        else:
            return -1
    if cards_1_sorted[1].point() == cards_2_sorted[1].point():
        return 0
    return 1 if cards_1_sorted[1].point() > cards_2_sorted[1].point() else -1


def _separate_high_low_factor(group: Dict[int, int], target_count) -> Tuple[List[int], List[int]]:
    high = []
    low = []
    for key, value in group.items():
        if value == target_count:
            high.append(key)
        else:
            low.append(key)
    assert len(high) > 0
    assert len(low) > 0
    return sorted(high, reverse=True), sorted(low, reverse=True)


def _compare_sorted_list(points_1: List[int], points_2: List[int]) -> int:
    assert len(points_1) == len(points_2)
    for i in range(len(points_1)):
        if points_1[i] > points_2[i]:
            return 1
        elif points_1[i] < points_2[i]:
            return -1
    return 0


def _compare_with_priority(
    cards_1_sorted: List[int], cards_2_sorted: List[int], factor_cnt: int) -> int:
    high_1, low_1 = _separate_high_low_factor(cards_1_sorted, factor_cnt)
    high_2, low_2 = _separate_high_low_factor(cards_2_sorted, factor_cnt)
    high_res = _compare_sorted_list(high_1, high_2)
    if high_res != 0:
        return high_res
    return _compare_sorted_list(low_1, low_2)


def _compare_reversed_points(cards_1_sorted: List[Card], cards_2_sorted: List[Card]) -> int:
    points_1 = [card.point() for card in cards_1_sorted]
    points_1.reverse()
    points_2 = [card.point() for card in cards_2_sorted]
    points_2.reverse()
    return _compare_sorted_list(points_1, points_2)
