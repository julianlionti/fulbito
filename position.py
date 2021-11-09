"""Position class"""
from enum import Enum


class Position(Enum):
    """Position enum"""
    GOAL_KEEPER = 0
    BACK_DEFENDER = 1
    DEFENDER = 2
    BACK_MIDFIELDER = 3
    MIDFIELDER = 4
    BACK_ATTACKER = 5
    ATTACKER = 6
