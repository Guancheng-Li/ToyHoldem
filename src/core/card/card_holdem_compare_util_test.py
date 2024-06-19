"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Unittest for card_holdem_compare_util
"""

from typing import List
import unittest

from core.card import card_holdem_compare_util
from core.card.card_holdem_type import CardType
from core.card.card_object import Card, CardColor


# pylint: disable=protected-access


def _create_cards(color: List[int], point: List[int]) -> List[Card]:
    assert len(color) == len(point), \
        'Cannot init cards with different size of color and point'
    cards = []
    for i in range(len(color)):
        cards.append(Card(CardColor(color[i]), point[i]))
    return cards


class CardHoldemCompareUtilTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_compare_2_group(self):
        for i in range(10):
            for j in range(10):
                if i != j:
                    expected = -1 if i < j else 1
                    self.assertEqual(
                        expected, card_holdem_compare_util.compare_2_diff_type(
                            CardType(i), CardType(j)))

    def test__compare_straight(self):
        # straight_flush obeys the same rule as straight.
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [5, 6, 7, 8, 9]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [6, 7, 8, 9, 10]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            -1, card_holdem_compare_util._compare_straight(cards_1, cards_2))
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [5, 6, 7, 8, 9]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [5, 6, 7, 8, 9]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            0, card_holdem_compare_util._compare_straight(cards_1, cards_2))
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [6, 7, 8, 9, 10]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [5, 6, 7, 8, 9]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            1, card_holdem_compare_util._compare_straight(cards_1, cards_2))

        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 2, 3, 4, 5]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [5, 6, 7, 8, 9]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            -1, card_holdem_compare_util._compare_straight(cards_1, cards_2))
        cards_1, cards_2 = cards_2, cards_1
        self.assertEqual(
            1, card_holdem_compare_util._compare_straight(cards_1, cards_2))

        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 10, 11, 12, 13]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [5, 6, 7, 8, 9]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            1, card_holdem_compare_util._compare_straight(cards_1, cards_2))
        cards_1, cards_2 = cards_2, cards_1
        self.assertEqual(
            -1, card_holdem_compare_util._compare_straight(cards_1, cards_2))

        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 2, 3, 4, 5]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [1, 10, 11, 12, 13]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            -1, card_holdem_compare_util._compare_straight(cards_1, cards_2))
        cards_1, cards_2 = cards_2, cards_1
        self.assertEqual(
            1, card_holdem_compare_util._compare_straight(cards_1, cards_2))
        self.assertEqual(
            0, card_holdem_compare_util._compare_straight(cards_1, cards_1))
        self.assertEqual(
            0, card_holdem_compare_util._compare_straight(cards_2, cards_2))

    def test_compare_four_of_a_kind(self):
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 1, 1, 1, 5]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [2, 2, 2, 2, 5]
        cards_2 = _create_cards(color_2, point_2)
        color_3 = [0, 1, 2, 3, 0]
        point_3 = [1, 1, 1, 1, 6]
        cards_3 = _create_cards(color_3, point_3)
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.FOUR_OF_A_KIND))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_3, CardType.FOUR_OF_A_KIND))
        self.assertEqual(
            1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_2, cards_3, CardType.FOUR_OF_A_KIND))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.FOUR_OF_A_KIND))

    def test_compare_full_house(self):
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 1, 1, 5, 5]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [2, 2, 2, 3, 3]
        cards_2 = _create_cards(color_2, point_2)
        color_3 = [0, 1, 2, 3, 0]
        point_3 = [1, 1, 1, 6, 6]
        cards_3 = _create_cards(color_3, point_3)
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.FULL_HOUSE))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_3, CardType.FULL_HOUSE))
        self.assertEqual(
            1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_2, cards_3, CardType.FULL_HOUSE))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.FULL_HOUSE))

    def test_compare_high_card(self):
        # flush obeys the same rule as straight.
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 3, 5, 7, 9]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [2, 4, 6, 8, 10]
        cards_2 = _create_cards(color_2, point_2)
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.HIGH_CARD))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.HIGH_CARD))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.FLUSH))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.FLUSH))

    def test_compare_three_of_a_kind(self):
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 1, 1, 5, 6]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [2, 2, 2, 1, 3]
        cards_2 = _create_cards(color_2, point_2)
        color_3 = [0, 1, 2, 3, 0]
        point_3 = [1, 1, 1, 6, 7]
        cards_3 = _create_cards(color_3, point_3)
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.THREE_OF_A_KIND))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_3, CardType.THREE_OF_A_KIND))
        self.assertEqual(
            1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_2, cards_3, CardType.THREE_OF_A_KIND))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.THREE_OF_A_KIND))

    def test_compare_two_pair(self):
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 1, 2, 2, 6]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [2, 2, 3, 3, 5]
        cards_2 = _create_cards(color_2, point_2)
        color_3 = [0, 1, 2, 3, 0]
        point_3 = [1, 1, 7, 7, 8]
        cards_3 = _create_cards(color_3, point_3)
        color_4 = [0, 1, 2, 3, 0]
        point_4 = [1, 1, 2, 2, 3]
        cards_4 = _create_cards(color_4, point_4)
        color_5 = [0, 1, 2, 3, 0]
        point_5 = [2, 2, 7, 7, 3]
        cards_5 = _create_cards(color_5, point_5)
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.TWO_PAIR))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_3, CardType.TWO_PAIR))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_2, cards_3, CardType.TWO_PAIR))
        self.assertEqual(
            1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_4, CardType.TWO_PAIR))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_3, cards_5, CardType.TWO_PAIR))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.TWO_PAIR))

    def test_compare_one_pair(self):
        color_1 = [0, 1, 2, 3, 0]
        point_1 = [1, 1, 3, 5, 6]
        cards_1 = _create_cards(color_1, point_1)
        color_2 = [0, 1, 2, 3, 0]
        point_2 = [2, 2, 7, 9, 3]
        cards_2 = _create_cards(color_2, point_2)
        color_3 = [0, 1, 2, 3, 0]
        point_3 = [1, 1, 2, 6, 7]
        cards_3 = _create_cards(color_3, point_3)
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_2, CardType.ONE_PAIR))
        self.assertEqual(
            -1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_3, CardType.ONE_PAIR))
        self.assertEqual(
            1, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_2, cards_3, CardType.ONE_PAIR))
        self.assertEqual(
            0, card_holdem_compare_util.compare_2_group_in_same_type(
                cards_1, cards_1, CardType.ONE_PAIR))


if __name__ == '__main__':
    unittest.main()
