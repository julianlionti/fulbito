"""Game test"""
from os import name
from dt import DT
from goal_keeper_skills import GoalKeeperSkills
from match import Match
from mentality import Mentality
from player import Player
from referee import Referee
from side import Side
from skills import Skill
from team import Position, Team
from random import randrange
from random import sample
from common_attrs import CommonAttrs
from utils import teamToPlayers


def createRandomPlayer(position: list, team: Team) -> Player:
    players = teamToPlayers(team)
    tshirt_numbers = [pla.tshirt_number for pla in players]

    tshirtNumber = randrange(1, 50)
    while(tshirtNumber in tshirt_numbers):
        tshirtNumber = randrange(1, 50)

    common = CommonAttrs()
    skills = Skill()
    return Player(
        common.createRandom(),
        skills.createRandom(),
        None,
        position,
        sample([Side.CENTER, Side.LEFT, Side.RIGHT], randrange(1, 3)),
        tshirtNumber
    )


def createRandomGoalKeeper() -> Player:
    common = CommonAttrs()
    return Player(
        common.createRandom(),
        None,
        GoalKeeperSkills(stamina=randrange(100), injury=randrange(100), aereal_ability=randrange(
            100), shot_stopping=randrange(100), rushing_out=randrange(100), physical=randrange(100), passing=randrange(100)),
        [Position.GOAL_KEEPER],
        None,
        1
    )


def createReferree() -> Referee:
    common = CommonAttrs()
    return Referee(attrs=common.createRandom(), experience=randrange(50, 70))


def test_configuring_match():

    team1 = Team(name="Racing Club", dt=DT(
        attrs=CommonAttrs(), mentality=Mentality.OFENSIVE))
    team2 = Team(name="All boys", dt=DT(
        attrs=CommonAttrs(), mentality=Mentality.OFENSIVE))

    for x in range(1):
        team1.add_position(createRandomGoalKeeper(), Position.GOAL_KEEPER)
        team2.add_position(createRandomGoalKeeper(), Position.GOAL_KEEPER)

    for x in range(4):
        team1.add_position(createRandomPlayer([Position.DEFENDER], team1), sample(
            [Position.BACK_DEFENDER, Position.DEFENDER], 1)[0])
        team2.add_position(createRandomPlayer([Position.DEFENDER], team2), sample(
            [Position.BACK_DEFENDER, Position.DEFENDER], 1)[0])

    for x in range(4):
        team1.add_position(createRandomPlayer([Position.MIDFIELDER], team1), sample(
            [Position.BACK_MIDFIELDER, Position.MIDFIELDER], 1)[0])
        team2.add_position(createRandomPlayer([Position.MIDFIELDER], team2), sample(
            [Position.BACK_MIDFIELDER, Position.MIDFIELDER], 1)[0])

    for x in range(2):
        team1.add_position(createRandomPlayer([Position.ATTACKER], team1), sample(
            [Position.BACK_ATTACKER, Position.ATTACKER], 1)[0])
        team2.add_position(createRandomPlayer([Position.ATTACKER], team2), sample(
            [Position.BACK_ATTACKER, Position.ATTACKER], 1)[0])

    assert len(teamToPlayers(team1)) == 11
    assert len(teamToPlayers(team2)) == 11

    match = Match(local=team1, visitor=team2, referee=createReferree())
    match.begin()


test_configuring_match()
