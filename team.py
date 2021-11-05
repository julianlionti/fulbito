"""Team class"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from position import Position
from player import Player


@dataclass_json
@dataclass()
class Team:
    """Team attrs"""
    # players = []
    goal_keeper: Player
    back_defenders = []
    defenders = []
    back_midfielder = []
    midfielder = []
    back_attackers = []
    attackers = []

    substitute = []

    def add_position(self, player, where_to: Position):
        """Add player to team"""
        print(self, player)
        if where_to == 1:
            print("Dale")
