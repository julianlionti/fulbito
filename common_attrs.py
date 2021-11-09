"""
Players attributes
"""
from dataclasses import dataclass, field
from foot import Foot
from names import get_first_name
from names import get_last_name
from random import randrange


@dataclass
class CommonAttrs:
    """Player attributes class."""
    name: str = field(init=False)
    surname: str = field(init=False)
    age: int = field(init=False)
    nationality: str = field(init=False)
    height: int = field(init=False)
    weight: int = field(init=False)
    foot: Foot = field(init=False)

    def createRandom(self):
        self.name = get_first_name(gender="male")
        self.surname = get_last_name()

        self.age = randrange(16, 45)
        self.nationality = "Argentina"
        self.weight = randrange(65, 110)
        self.height = randrange(155, 210)
        self.foot = randrange(1, 2)

        return self
