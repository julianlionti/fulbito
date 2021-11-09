"""Team Stadistics class"""
from dataclasses import dataclass

from player import Player
from player_stadistics import PlayerStadistics


@dataclass
class TeamStadistics:
    """Team Stadistics attrs"""
    players: dict[Player, PlayerStadistics]
