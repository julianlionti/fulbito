"""
GoalKeeperSkills for pitch players
"""
from dataclasses import dataclass

from common_skills import CommonSkills


@dataclass
class GoalKeeperSkills(CommonSkills):
    """GoalKeeperSkills ptch player."""
    aereal_ability: int
    shot_stopping: int
    rushing_out: int
    stamina: int
    shooting: int
    physical: int
    passing: int
