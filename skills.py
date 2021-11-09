"""
Skills for pitch players
"""
from dataclasses import dataclass, field
from random import randrange
from common_skills import CommonSkills


@dataclass
class Skill(CommonSkills):
    """Skills for pitch attrs."""
    pace: int = 0
    dribbling: int = 0
    defending: int = 0
    shooting: int = 0
    physical: int = 0
    passing: int = 0
    stamina: int = 0

    def createRandom(self):
        self.stamina = randrange(100)
        self.injury = randrange(100)
        self.pace = randrange(100)
        self.dribbling = randrange(100)
        self.defending = randrange(100)
        self.shooting = randrange(100)
        self.physical = randrange(100)
        self.passing = randrange(100)
