"""Match class"""
from dataclasses import dataclass, field
from random import randrange
from actions import Actions
from history import History
from player import Player
from referee import Referee
from team import Team
from utils import randomZeroOne

from time import sleep


@dataclass
class Match:
    """Match attrs"""
    local: Team
    visitor: Team
    referee: Referee
    ball_player_position: Player = None
    ball_team_position: Team = None
    history: list[History] = field(default_factory=list)
    time_length: int = 45
    is_stopped: bool = False

    def drawKickoff(self):
        print("Sorteando saque inicial")
        ball_team_position = randomZeroOne() == 0 and self.local or self.visitor
        self.history.append(History(action=Actions.KICK_OFF,
                            time=0, team=ball_team_position))

        print("Saca",  ball_team_position.name)
        self.startMatch()

    def startMatch(self):
        print("Empezó el partido")
        self.startTime(1)

    def startTime(self, which):
        print("Arranca el %d tiempo" % (which))
        count = 0
        aditional = 0
        while (count <= 45 + aditional):
            print("Minuto %d" % (count))
            if count == 44:
                aditional = randrange(0, which == 1 and 2 or 5)
            count = count + 1
            sleep(0.5)

        if which == 1:
            self.halfTime()

        if which == 2:
            self.end()

    def halfTime(self):
        print("Entretiempo")
        sleep(1)
        self.startTime(2)

    def end(self):
        print("Terminó")
        print("Ganó %s" % (self.local.name))
