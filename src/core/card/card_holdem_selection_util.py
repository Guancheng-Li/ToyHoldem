"""
Authors: guanchenglichina@qq.com (Guancheng Li)

To select the most score 5 cards from 7 cards.
"""

from typing import List

from core.card.card_holdem_type import card_type_of_5_cards
from core.card.card_holdem_compare_util import compare_2_group_in_same_type
from core.card.card_object import Card


def select_high_score_cards(cards: List[Card]) -> List[Card]:
    assert len(cards) == 7
    highest_type = None
    candidate = []
    for i in range(7):
        for j in range(7):
            if i >= j:
                continue
            tmp_list = [cards[k] for k in range(7) if k not in [i, j]]
            tmp_list_type = card_type_of_5_cards(tmp_list)
            if highest_type is None:
                highest_type = tmp_list_type
                candidate.append(tmp_list)
                continue
            if tmp_list_type.value > highest_type.value:
                highest_type = tmp_list_type
                candidate = [tmp_list]
            elif tmp_list_type.value == highest_type.value:
                candidate.append(tmp_list)
    best_candidate = candidate[0]
    for item in candidate[1:]:
        if compare_2_group_in_same_type(
            item, best_candidate, highest_type) > 0:
            best_candidate = item
    return best_candidate
