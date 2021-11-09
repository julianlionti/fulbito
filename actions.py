from dataclasses import dataclass
from enum import Enum


@dataclass
class Actions(Enum):
    KICK_OFF = 0
    PASS = 1
    LONG_PASS = 2
    DRIBBLE = 3
    TACKLE = 4
    FOUL = 5
    LONG_SHOOT = 6
    SHOOT = 7
    CENTER = 8
