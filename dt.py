"""DT class"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_attrs import CommonAttrs


@dataclass_json
@dataclass
class DT:
    """DT class"""
    attrs: CommonAttrs
