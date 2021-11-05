"""
Players attributes
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from foot import Foot


@dataclass_json
@dataclass
class CommonAttrs:
    """Player attributes class."""
    name: str
    surname: str
    age: int
    nationality: str
    height: int
    weight: int
    foot: Foot
