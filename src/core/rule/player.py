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
    # TODO(Guancheng Li): Maybe add viewer or god_viewer.


class PlayerState(enum.Enum):
    ALIVE = 0
    FOLD = 1
    ALL_IN = 2


class Player:
    """The player of game."""
    _NEXT_PLAYER_ID = 0

    def __init__(self, ip: str):
        self._id = Player._NEXT_PLAYER_ID
        Player._NEXT_PLAYER_ID += 1
        self._ip = ip
        self._role = Role.NORMAL
        self._state = PlayerState.ALIVE
        self._score = 0

    def role(self) -> Role:
        return self._role

    def is_alive(self) -> bool:
        return self._state == PlayerState.ALIVE

    def set_dealer(self):
        self._role = Role.DEALER

    def set_big_blind(self):
        self._role = Role.BIG_BLIND

    def set_small_blind(self):
        self._role = Role.SMALL_BLIND

    def add_score(self, score: int):
        """End of game or initialize."""
        self._score += score

    def set_fold(self):
        self._state = PlayerState.FOLD

    def action(self):
        # TODO
