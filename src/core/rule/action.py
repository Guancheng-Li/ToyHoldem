"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The actions for one candidate to execute.
"""

import enum


class Action(enum.Enum):
    FOLD = 0
    CALL = 1
    RAISE = 2
    CHECK = 3
    ALL_IN = 4
