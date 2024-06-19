"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The state machine of round.
"""

import enum


class RoundState(enum.Enum):
    PRE_FLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
