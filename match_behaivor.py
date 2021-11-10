from dataclasses import dataclass, field
from random import randrange
from time import sleep
from actions import Actions

from history import History
from player import Player
from team import Team


@dataclass
class MatchBehaivor():
    history: list[History] = field(default_factory=list)
    ball_player_position: Player = None
    ball_team_position: Team = None

    def time_loop(self, which: int):
        count = 0
        aditional = 0
        while (count <= self.time_length + aditional):
            print("Minuto %d" % (count))
            if count == (self.time_length - 1):
                aditional = randrange(0, which == 1 and 2 or 5)

            inner_count = 0
            next_action = self.calculate_next_action(count + inner_count)
            while (next_action != None):
                next_action = self.calculate_next_action(count + inner_count)

                if inner_count == 0.6:
                    count = count + 1

                inner_count = inner_count + 0.1
                sleep(0.5)

            count = count + 1
            print([{"time": hist.time, "action": hist.action, "team": hist.team.name}
                  for hist in self.history])
            sleep(1)

    def calculate_next_action(self, minute: int) -> Actions:
        last_action = self.history[-1]

        if last_action.action is Actions.KICK_OFF:
            next_action = Actions.PASS
            keep_posesion = True
        else:
            next_action = None
            keep_posesion = True

        if last_action.action is not next_action:
            self.history.append(History(action=next_action, time=minute,
                                        team=keep_posesion and self.ball_team_position or None))

        return next_action
