"""Match Stadistics class"""
from dataclasses import dataclass

from team_stadistics import TeamStadistics


@dataclass
class MatchStadistics:
    """Match Stadistics attrs"""
    local: TeamStadistics
    visitor: TeamStadistics
