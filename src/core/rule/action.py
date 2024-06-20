"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The actions for one candidate to execute.
"""

import enum


class ActionType(enum.Enum):
    FOLD = 0  # Surrendering the pot.
    CALL = 1  # Matching a bet.
    RAISE = 2  # Increasing the size of bet.
    CHECK = 3  # Passing the action to the next player.
    BET = 4  # Putting chips into the pot.
    ALL_IN = 5  # Putting all chips into the pot.

class Action():
    def __init__(self, action_type: ActionType, amount: int = 0):
        self._type = action_type
        self._amount = amount

    def type(self) -> ActionType:
        return self._type
