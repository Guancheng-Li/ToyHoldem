"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The player of game candidates.
"""

import enum


class Role(enum.Enum):
    NORMAL = 0
    DEALER = 1
    SMALL_BLIND = 2
    BIG_BLIND = 3
    # TODO(Guancheng Li): Maybe add viewer.


class PlayerState(enum.Enum):
    ALIVE = 0
    FOLD = 1
    ALL_IN = 2


class Player:
    """The player of game."""
    def __init__(self, id: int, role: Role):
        self._id = id
        self._role = role
        self._state = PlayerState.ALIVE

