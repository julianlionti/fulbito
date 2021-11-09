"""Game test"""
from os import name
from goal_keeper_skills import GoalKeeperSkills
from match import Match
from player import Player
from referee import Referee
from side import Side
from skills import Skill
from team import Position, Team
from random import randrange
from random import sample
import names
from common_attrs import CommonAttrs


def createRandomPlayer(position: list) -> Player:
    common = CommonAttrs()
    return Player(
        common.createRandom(),
        Skill(stamina=randrange(100), injury=randrange(100), pace=randrange(100), dribbling=randrange(100),
              defending=randrange(100), shooting=randrange(100), physical=randrange(100), passing=randrange(100)),
        None,
        position,
        sample([Side.CENTER, Side.LEFT, Side.RIGHT], randrange(1, 3))
    )


def createRandomGoalKeeper() -> Player:
    common = CommonAttrs()
    return Player(
        common.createRandom(),
        None,
        GoalKeeperSkills(stamina=randrange(100), injury=randrange(100), aereal_ability=randrange(
            100), shot_stopping=randrange(100), rushing_out=randrange(100), physical=randrange(100), passing=randrange(100)),
        [Position.GOAL_KEEPER],
        None
    )


def createReferree() -> Referee:
    common = CommonAttrs()
    return Referee(attrs=common.createRandom(), experience=randrange(50, 70))


def test_configuring_match():

    team1 = Team(name="Racing Club")
    team2 = Team(name="All boys")

    for x in range(1):
        team1.add_position(createRandomGoalKeeper(), Position.GOAL_KEEPER)
        team2.add_position(createRandomGoalKeeper(), Position.GOAL_KEEPER)

    for x in range(4):
        team1.add_position(createRandomPlayer([Position.DEFENDER]), sample(
            [Position.BACK_DEFENDER, Position.DEFENDER], 1)[0])
        team2.add_position(createRandomPlayer([Position.DEFENDER]), sample(
            [Position.BACK_DEFENDER, Position.DEFENDER], 1)[0])

    for x in range(4):
        team1.add_position(createRandomPlayer([Position.MIDFIELDER]), sample(
            [Position.BACK_MIDFIELDER, Position.MIDFIELDER], 1)[0])
        team2.add_position(createRandomPlayer([Position.MIDFIELDER]), sample(
            [Position.BACK_MIDFIELDER, Position.MIDFIELDER], 1)[0])

    for x in range(2):
        team1.add_position(createRandomPlayer([Position.ATTACKER]), sample(
            [Position.BACK_ATTACKER, Position.ATTACKER], 1)[0])
        team2.add_position(createRandomPlayer([Position.ATTACKER]), sample(
            [Position.BACK_ATTACKER, Position.ATTACKER], 1)[0])

    assert team1.goal_keeper != None
    assert team2.goal_keeper != None

    assert len(team1.defenders) + len(team1.back_defenders) == 4
    assert len(team1.midfielder) + len(team1.back_midfielder) == 4
    assert len(team1.attackers) + len(team1.back_attackers) == 2

    match = Match(local=team1, visitor=team2, referee=createReferree())
    match.drawKickoff()


test_configuring_match()
