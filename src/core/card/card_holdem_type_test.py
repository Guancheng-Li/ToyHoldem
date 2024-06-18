"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Unittest for card_holdem_type
"""

from typing import List
import unittest

from core.card import card_holdem_type
from core.card.card_object import Card, CardColor, sort_card_by_point


# pylint: disable=protected-access


def _create_cards(color: List[int], point: List[int]) -> List[Card]:
    assert len(color) == len(point), 'Cannot init cards with different size of color and point'
    cards = []
    for i in range(len(color)):
        cards.append(Card(CardColor(color[i]), point[i]))
    return cards


class CardHoldemTypeTest(unittest.TestCase):

    def setUp(self) -> None:
        cards_list = []
        cards_group_list = []
        sorted_cards_list = []
        # HIGH_CARD
        color_0 = [0, 0, 1, 2, 3]
        point_0 = [1, 2, 3, 4, 7]
        cards_0 = _create_cards(color_0, point_0)
        cards_list.append(cards_0)
        sorted_cards_0 = sort_card_by_point(cards_0)
        sorted_cards_list.append(sorted_cards_0)
        cards_group_0 = card_holdem_type.group_by_point(cards_0)
        cards_group_list.append(cards_group_0)
        # ONE_PAIR
        color_1 = [0, 0, 1, 2, 3]
        point_1 = [1, 2, 1, 4, 5]
        cards_1 = _create_cards(color_1, point_1)
        cards_list.append(cards_1)
        sorted_cards_1 = sort_card_by_point(cards_1)
        sorted_cards_list.append(sorted_cards_1)
        cards_group_1 = card_holdem_type.group_by_point(cards_1)
        cards_group_list.append(cards_group_1)
        # TWO_PAIR
        color_2 = [0, 0, 1, 2, 3]
        point_2 = [1, 2, 1, 2, 5]
        cards_2 = _create_cards(color_2, point_2)
        cards_list.append(cards_2)
        sorted_cards_2 = sort_card_by_point(cards_2)
        sorted_cards_list.append(sorted_cards_2)
        cards_group_2 = card_holdem_type.group_by_point(cards_2)
        cards_group_list.append(cards_group_2)
        # THREE_OF_A_KIND
        color_3 = [0, 3, 1, 2, 3]
        point_3 = [1, 1, 1, 2, 5]
        cards_3 = _create_cards(color_3, point_3)
        cards_list.append(cards_3)
        sorted_cards_3 = sort_card_by_point(cards_3)
        sorted_cards_list.append(sorted_cards_3)
        cards_group_3 = card_holdem_type.group_by_point(cards_3)
        cards_group_list.append(cards_group_3)
        # STRAIGHT
        color_4 = [0, 3, 1, 2, 3]
        point_4 = [1, 2, 3, 4, 5]
        cards_4 = _create_cards(color_4, point_4)
        cards_list.append(cards_4)
        sorted_cards_4 = sort_card_by_point(cards_4)
        sorted_cards_list.append(sorted_cards_4)
        cards_group_4 = card_holdem_type.group_by_point(cards_4)
        cards_group_list.append(cards_group_4)
        # FLUSH
        color_5 = [0, 0, 0, 0, 0]
        point_5 = [1, 7, 11, 2, 5]
        cards_5 = _create_cards(color_5, point_5)
        cards_list.append(cards_5)
        sorted_cards_5 = sort_card_by_point(cards_5)
        sorted_cards_list.append(sorted_cards_5)
        cards_group_5 = card_holdem_type.group_by_point(cards_5)
        cards_group_list.append(cards_group_5)
        # FULL_HOUSE
        color_6 = [0, 3, 1, 2, 3]
        point_6 = [1, 1, 1, 5, 5]
        cards_6 = _create_cards(color_6, point_6)
        cards_list.append(cards_6)
        sorted_cards_6 = sort_card_by_point(cards_6)
        sorted_cards_list.append(sorted_cards_6)
        cards_group_6 = card_holdem_type.group_by_point(cards_6)
        cards_group_list.append(cards_group_6)
        # FOUR_OF_A_KIND
        color_7 = [0, 3, 1, 2, 3]
        point_7 = [1, 1, 1, 1, 5]
        cards_7 = _create_cards(color_7, point_7)
        cards_list.append(cards_7)
        sorted_cards_7 = sort_card_by_point(cards_7)
        sorted_cards_list.append(sorted_cards_7)
        cards_group_7 = card_holdem_type.group_by_point(cards_7)
        cards_group_list.append(cards_group_7)
        # STRAIGHT_FLUSH
        color_8 = [0, 0, 0, 0, 0]
        point_8 = [1, 2, 3, 4, 5]
        cards_8 = _create_cards(color_8, point_8)
        cards_list.append(cards_8)
        sorted_cards_8 = sort_card_by_point(cards_8)
        sorted_cards_list.append(sorted_cards_8)
        cards_group_8 = card_holdem_type.group_by_point(cards_8)
        cards_group_list.append(cards_group_8)
        # ROYAL_FLUSH
        color_9 = [0, 0, 0, 0, 0]
        point_9 = [10, 12, 11, 13, 1]
        cards_9 = _create_cards(color_9, point_9)
        cards_list.append(cards_9)
        sorted_cards_9 = sort_card_by_point(cards_9)
        sorted_cards_list.append(sorted_cards_9)
        cards_group_9 = card_holdem_type.group_by_point(cards_9)
        cards_group_list.append(cards_group_9)
        self.cards_list = cards_list
        self.sorted_cards_list = sorted_cards_list
        self.cards_group_list = cards_group_list

    def test__is_one_pair(self):
        positive_index = set([1])
        for i, item in enumerate(self.cards_group_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_one_pair(item))
            else:
                self.assertFalse(card_holdem_type._is_one_pair(item))

    def test__is_two_pair(self):
        positive_index = set([2])
        for i, item in enumerate(self.cards_group_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_two_pair(item))
            else:
                self.assertFalse(card_holdem_type._is_two_pair(item))

    def test__is_three_of_a_kind(self):
        positive_index = set([3])
        for i, item in enumerate(self.cards_group_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_three_of_a_kind(item))
            else:
                self.assertFalse(card_holdem_type._is_three_of_a_kind(item))

    def test__is_straight_basic(self):
        positive_index = set([4, 8, 9])
        for i, item in enumerate(self.sorted_cards_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_straight_basic(item))
            else:
                self.assertFalse(card_holdem_type._is_straight_basic(item), msg=f'{i}')

        color_0 = [0, 1, 2, 3, 0]
        point_0 = [2, 3, 4, 5, 1]
        cards_0 = _create_cards(color_0, point_0)
        sorted_cards_0 = sort_card_by_point(cards_0)
        self.assertTrue(card_holdem_type._is_straight_basic(sorted_cards_0))

        color_1 = [0, 1, 2, 3, 0]
        point_1 = [11, 10, 9, 13, 12]
        cards_1 = _create_cards(color_1, point_1)
        sorted_cards_1 = sort_card_by_point(cards_1)
        self.assertTrue(card_holdem_type._is_straight_basic(sorted_cards_1))

        color_2 = [0, 1, 2, 3, 0]
        point_2 = [11, 1, 12, 13, 10]
        cards_2 = _create_cards(color_2, point_2)
        sorted_cards_2 = sort_card_by_point(cards_2)
        self.assertTrue(card_holdem_type._is_straight_basic(sorted_cards_2))

        color_3 = [0, 1, 2, 3, 0]
        point_3 = [11, 2, 12, 13, 1]
        cards_3 = _create_cards(color_3, point_3)
        sorted_cards_3 = sort_card_by_point(cards_3)
        self.assertFalse(card_holdem_type._is_straight_basic(sorted_cards_3))

    def test__is_flush_basic(self):
        positive_index = set([5, 8, 9])
        for i, item in enumerate(self.sorted_cards_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_flush_basic(item))
            else:
                self.assertFalse(card_holdem_type._is_flush_basic(item))

    def test__is_full_house(self):
        positive_index = set([6])
        for i, item in enumerate(self.cards_group_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_full_house(item))
            else:
                self.assertFalse(card_holdem_type._is_full_house(item))

    def test__is_four_of_a_kind(self):
        positive_index = set([7])
        for i, item in enumerate(self.cards_group_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_four_of_a_kind(item))
            else:
                self.assertFalse(card_holdem_type._is_four_of_a_kind(item))

    def test__is_straight_flush_basic(self):
        positive_index = set([8, 9])
        for i, item in enumerate(self.sorted_cards_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_straight_flush_basic(item))
            else:
                self.assertFalse(card_holdem_type._is_straight_flush_basic(item))

    def test__is_royal_flush(self):
        positive_index = set([9])
        for i, item in enumerate(self.sorted_cards_list):
            if i in positive_index:
                self.assertTrue(card_holdem_type._is_royal_flush(item))
            else:
                self.assertFalse(card_holdem_type._is_royal_flush(item))

    def test_card_type_of_5_cards(self):
        for i, item in enumerate(self.cards_list):
            self.assertEqual(
                card_holdem_type.card_type_of_5_cards(item),
                card_holdem_type.CardType(i))


if __name__ == '__main__':
    unittest.main()
