"""
Authors: guanchenglichina@qq.com (Guancheng Li)

Unittest for card_holdem_selection_util
"""

from typing import List
import unittest

from core.card import card_holdem_selection_util
from core.card.card_object import Card, CardColor


# pylint: disable=protected-access


def _create_cards(color: List[int], point: List[int]) -> List[Card]:
    assert len(color) == len(point), 'Cannot init cards with different size of color and point'
    cards = []
    for i in range(len(color)):
        cards.append(Card(CardColor(color[i]), point[i]))
    return cards


def _encode_cards(cards: List[Card]) -> str:
    return ', '.join([item.encode() for item in cards])


def _check_expected_cards(cards: List[Card], expected_cards: List[Card]) -> bool:
    # NOTE: unique_id() is unique for a card, but should not use here.
    #       Because multiple best combination may be possible, in this case, \
    #       the expected_cards only contains the key cards, in other words, \
    #       len(cards) >= len(expected_cards).
    card_unique_ids = {item.unique_id() for item in cards}
    for item in expected_cards:
        if item.unique_id() not in card_unique_ids:
            return False, \
                f'Expected card {item.encode()} is not in selected cards({_encode_cards(cards)}).'
    return True, None


class CardHoldemCompareUtilTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_select_cards(self):
        # ROYAL_FLUSH
        color_0 = [0, 0, 0, 0, 0, 1, 2]
        point_0 = [10, 11, 12, 13, 1, 1, 1]
        cards_0 = _create_cards(color_0, point_0)
        selected_cards_0 = card_holdem_selection_util.select_high_score_cards(cards_0)
        expected_cards_0 = cards_0[0:5]
        res, error_msg = _check_expected_cards(selected_cards_0, expected_cards_0)
        self.assertTrue(res, msg=error_msg)

        # STRAIGHT_FLUSH
        color_1 = [0, 0, 0, 0, 0, 1, 2]
        point_1 = [10, 11, 12, 13, 9, 9, 9]
        cards_1 = _create_cards(color_1, point_1)
        selected_cards_1 = card_holdem_selection_util.select_high_score_cards(cards_1)
        expected_cards_1 = cards_1[0:5]
        res, error_msg = _check_expected_cards(selected_cards_1, expected_cards_1)
        self.assertTrue(res, msg=error_msg)

        # FOUR_OF_A_KIND
        color_2 = [0, 1, 2, 3, 0, 1, 2]
        point_2 = [9, 10, 10, 10, 10, 9, 9]
        cards_2 = _create_cards(color_2, point_2)
        selected_cards_2 = card_holdem_selection_util.select_high_score_cards(cards_2)
        expected_cards_2 = cards_2[1:5]
        res, error_msg = _check_expected_cards(selected_cards_2, expected_cards_2)
        self.assertTrue(res, msg=error_msg)

        # FULL_HOUSE
        color_3 = [0, 1, 2, 3, 0, 1, 2]
        point_3 = [9, 9, 9, 13, 13, 11, 11]
        cards_3 = _create_cards(color_3, point_3)
        selected_cards_3 = card_holdem_selection_util.select_high_score_cards(cards_3)
        expected_cards_3 = cards_3[0:5]
        res, error_msg = _check_expected_cards(selected_cards_3, expected_cards_3)
        self.assertTrue(res, msg=error_msg)

        # FLUSH
        color_4 = [0, 0, 0, 0, 0, 0, 0]
        point_4 = [13, 12, 11, 9, 8, 7, 1]
        cards_4 = _create_cards(color_4, point_4)
        selected_cards_4 = card_holdem_selection_util.select_high_score_cards(cards_4)
        expected_cards_4 = cards_4[0:5]
        res, error_msg = _check_expected_cards(selected_cards_4, expected_cards_4)
        self.assertTrue(res, msg=error_msg)

        # STRAIGHT
        color_5 = [0, 1, 3, 2, 0, 1, 0]
        point_5 = [13, 12, 11, 10, 1, 9, 8]
        cards_5 = _create_cards(color_5, point_5)
        selected_cards_5 = card_holdem_selection_util.select_high_score_cards(cards_5)
        expected_cards_5 = cards_5[0:5]
        res, error_msg = _check_expected_cards(selected_cards_5, expected_cards_5)
        self.assertTrue(res, msg=error_msg)

        # THREE_OF_A_KIND
        color_6 = [0, 1, 3, 2, 0, 1, 0]
        point_6 = [13, 13, 13, 10, 9, 8, 7]
        cards_6 = _create_cards(color_6, point_6)
        selected_cards_6 = card_holdem_selection_util.select_high_score_cards(cards_6)
        expected_cards_6 = cards_6[0:5]
        res, error_msg = _check_expected_cards(selected_cards_6, expected_cards_6)
        self.assertTrue(res, msg=error_msg)

        # TWO_PAIR
        color_7 = [0, 1, 3, 2, 0, 1, 0]
        point_7 = [13, 13, 12, 12, 11, 11, 8]
        cards_7 = _create_cards(color_7, point_7)
        selected_cards_7 = card_holdem_selection_util.select_high_score_cards(cards_7)
        expected_cards_7 = cards_7[0:4]
        res, error_msg = _check_expected_cards(selected_cards_7, expected_cards_7)
        self.assertTrue(res, msg=error_msg)

        # ONE_PAIR
        color_8 = [0, 1, 3, 2, 0, 1, 0]
        point_8 = [12, 12, 13, 11, 8, 6, 3]
        cards_8 = _create_cards(color_8, point_8)
        selected_cards_8 = card_holdem_selection_util.select_high_score_cards(cards_8)
        expected_cards_8 = cards_8[0:5]
        res, error_msg = _check_expected_cards(selected_cards_8, expected_cards_8)
        self.assertTrue(res, msg=error_msg)

        # HIGH_CARD
        color_9 = [0, 1, 3, 2, 0, 1, 0]
        point_9 = [12, 9, 13, 11, 8, 1, 3]
        cards_9 = _create_cards(color_9, point_9)
        selected_cards_9 = card_holdem_selection_util.select_high_score_cards(cards_9)
        expected_cards_9 = cards_9[0:5]
        res, error_msg = _check_expected_cards(selected_cards_9, expected_cards_9)
        self.assertTrue(res, msg=error_msg)

        # FOUR_OF_A_KIND, better choice.
        color_10 = [0, 1, 2, 3, 0, 1, 2]
        point_10 = [13, 10, 10, 10, 10, 9, 9]
        cards_10 = _create_cards(color_10, point_10)
        selected_cards_10 = card_holdem_selection_util.select_high_score_cards(cards_10)
        expected_cards_10 = cards_10[0:5]
        res, error_msg = _check_expected_cards(selected_cards_10, expected_cards_10)
        self.assertTrue(res, msg=error_msg)

        # FULL_HOUSE, better choice.
        color_11 = [0, 1, 2, 3, 0, 1, 2]
        point_11 = [9, 9, 9, 8, 8, 8, 11]
        cards_11 = _create_cards(color_11, point_11)
        selected_cards_11 = card_holdem_selection_util.select_high_score_cards(cards_11)
        expected_cards_11 = cards_11[0:3]
        res, error_msg = _check_expected_cards(selected_cards_11, expected_cards_11)
        self.assertTrue(res, msg=error_msg)

        # TWO_PAIR, better choice.
        color_12 = [0, 1, 3, 2, 0, 1, 0]
        point_12 = [13, 13, 12, 12, 11, 1, 7]
        cards_12 = _create_cards(color_12, point_12)
        selected_cards_12 = card_holdem_selection_util.select_high_score_cards(cards_12)
        expected_cards_12 = cards_12[0:5]
        res, error_msg = _check_expected_cards(selected_cards_12, expected_cards_12)
        self.assertTrue(res, msg=error_msg)


if __name__ == '__main__':
    unittest.main()
