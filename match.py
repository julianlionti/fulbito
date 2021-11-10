"""Match class"""
from dataclasses import dataclass, field
from random import randrange
from typing import Union
from actions import Actions
from history import History
from locality import Locality
from match_stadistics import MatchStadistics
from player import Player
from player_stadistics import PlayerStadistics
from referee import Referee
from team import Team
from team_stadistics import TeamStadistics
from utils import randomZeroOne
from utils import teamToPlayers

from time import sleep


@dataclass(init=False)
class Match:
    """Match attrs"""
    local: Team
    visitor: Team
    referee: Referee

    ball_player_position: Player = None
    ball_team_position: Team = None

    history: list[History] = field(default_factory=list)
    stadistics: MatchStadistics = None

    time_length: int = 45
    is_stopped: bool = False

    def __init__(self, local: Team, visitor: Team, referee: Referee) -> None:
        self.local = local
        self.visitor = visitor
        self.referee = referee
        self.history = []

        localStadistics = TeamStadistics(players=dict.fromkeys(
            [pla.tshirt_number for pla in teamToPlayers(local)], PlayerStadistics()))

        visitorStadistics = TeamStadistics(players=dict.fromkeys(
            [pla.tshirt_number for pla in teamToPlayers(visitor)], PlayerStadistics()))

        self.stadistics = MatchStadistics(
            local=localStadistics, visitor=visitorStadistics)

    def begin(self):
        self.drawKickoff()

    def drawKickoff(self):
        print("Sorteando saque inicial")
        self.ball_team_position = randomZeroOne(
        ) == Locality.LOCAL and self.local or self.visitor
        self.history.append(History(action=Actions.KICK_OFF,
                            time=0, team=self.ball_team_position))

        print("Saca",  self.ball_team_position.name)
        self.startMatch()

    def startMatch(self):
        print("Empezó el partido")
        self.startTime(1)

    def startTime(self, which):
        print("Arranca el %d tiempo" % (which))
        count = 0
        aditional = 0
        while (count <= self.time_length + aditional):
            print("Minuto %d" % (count))
            if count == (self.time_length - 1):
                aditional = randrange(0, which == 1 and 2 or 5)
            count = count + 1
            action = self.something_happen()
            while(action != None):
                self.ball_team_position.do_action()

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

    def something_happen(self) -> Union[Actions, None]:
        last_action = self.history[-1]

        if last_action.action == Actions.KICK_OFF:
            next_action = Actions.PASS
        else:
            next_action = None

        print(next_action)
        return next_action
