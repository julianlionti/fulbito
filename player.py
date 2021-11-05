"""Player class"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_attrs import CommonAttrs
from goal_keeper_skills import GoalKeeperSkills
from skills import Skill


@dataclass_json
@dataclass
class Player:
    """Player class"""
    attrs: CommonAttrs
    skills: Skill
    gk_skills: GoalKeeperSkills
    positions: list
