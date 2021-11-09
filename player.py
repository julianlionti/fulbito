"""Player class"""
from dataclasses import dataclass
from common_attrs import CommonAttrs
from goal_keeper_skills import GoalKeeperSkills
from player_stadistics import PlayerStadistics
from position import Position
from side import Side
from skills import Skill


@dataclass
class Player:
    """Player class"""
    attrs: CommonAttrs
    skills: Skill
    gk_skills: GoalKeeperSkills
    positions: list[Position]
    side: list[Side]
    tshirt_number: int
