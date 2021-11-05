"""
Skills for pitch players
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_skills import CommonSkills


@dataclass_json
@dataclass
class Skill(CommonSkills):
    """Skills for pitch attrs."""
    pace: int
    dribbling: int
    defending: int
    shooting: int
    physical: int
    passing: int
    stamina: int
