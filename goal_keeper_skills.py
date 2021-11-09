"""
GoalKeeperSkills for pitch players
"""
from dataclasses import dataclass
from common_skills import CommonSkills


@dataclass
class GoalKeeperSkills(CommonSkills):
    """GoalKeeperSkills ptch player."""
    aereal_ability: int = 0
    shot_stopping: int = 0
    rushing_out: int = 0
    stamina: int = 0
    # shooting: int
    physical: int = 0
    passing: int = 0
