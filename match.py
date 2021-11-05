"""Match class"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass()
class Match:
    """Match attrs"""
    time_length = 45
    teams = []
