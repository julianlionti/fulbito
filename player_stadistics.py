"""PlayerStadistics class"""
from dataclasses import dataclass


@dataclass
class PlayerStadistics:
    """PlayerStadistics attrs"""
    goals: int = 0
    shoots: int = 0
    shootsSuccesfully: int = 0
    passes: int = 0
    passesSuccesfully: int = 0
    fouls: int = 0
    yellowCards: int = 0
    redCard: int = 0
