"""
CommonSkills attributes
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class CommonSkills:
    """CommonSkills attributes class."""
    stamina: int
    injury: int
    # morale :int
