"""History class"""
from dataclasses import dataclass
from actions import Actions
from team import Team


@dataclass
class History:
    """History attrs"""
    action: Actions
    time: int
    team: Team = None
