from random import randrange
from player import Player

from team import Team


def teamToPlayers(team: Team) -> list[Player]:
    return [team.goal_keeper] + team.back_defenders + team.defenders + team.back_midfielder + team.midfielder + team.back_attackers + team.attackers


def randomZeroOne():
    rand = randrange(0, 100)
    zeroOne = rand / 100
    if zeroOne > 0.49:
        return 1
    else:
        return 0
