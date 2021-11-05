"""Game test"""
from os import name
from player import Player
from skills import Skill
from team import Position
from random import randrange
import names
from common_attrs import CommonAttrs


def createRandomPlayer(position: list) -> Player:
    return Player(
        CommonAttrs(name=names.get_first_name(gender="male"), surname=names.get_last_name(),
                    age=randrange(16, 45), nationality="Argentina",
                    weight=randrange(65, 110), height=randrange(155, 210), foot=randrange(1, 2)),
        Skill(stamina=randrange(100), injury=randrange(100), pace=randrange(100), dribbling=randrange(100),
              defending=randrange(100), shooting=randrange(100), physical=randrange(100), passing=randrange(100)),
        None,
        position
    )


def test_configuring_match():

    players = []
    for x in range(8):
        players.append(createRandomPlayer([Position.DEFENDER]))

    for x in range(8):
        players.append(createRandomPlayer([Position.MIDFIELDER]))

    for x in range(4):
        players.append(createRandomPlayer([Position.ATTACKER]))

    for player in players:
        print(player)

    assert True
