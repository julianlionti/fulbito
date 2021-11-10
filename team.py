"""Team class"""
from dataclasses import dataclass, field
from random import randrange
from time import sleep
from dt import DT

from position import Position
from player import Player


@dataclass()
class Team:
    """Team attrs"""
    name: str
    dt: DT

    goal_keeper: Player = None
    back_defenders: list[Player] = field(default_factory=list)
    defenders: list[Player] = field(default_factory=list)
    back_midfielder: list[Player] = field(default_factory=list)
    midfielder: list[Player] = field(default_factory=list)
    back_attackers: list[Player] = field(default_factory=list)
    attackers: list[Player] = field(default_factory=list)

    substitutes: list[Player] = field(default_factory=list)

    def add_position(self, player: Player, where_to: Position):
        if where_to == Position.GOAL_KEEPER:
            self.goal_keeper = player

        if where_to == Position.BACK_DEFENDER:
            self.back_defenders.append(player)

        if where_to == Position.DEFENDER:
            self.defenders.append(player)

        if where_to == Position.BACK_MIDFIELDER:
            self.back_midfielder.append(player)

        if where_to == Position.MIDFIELDER:
            self.midfielder.append(player)

        if where_to == Position.BACK_ATTACKER:
            self.back_attackers.append(player)

        if where_to == Position.ATTACKER:
            self.attackers.append(player)

