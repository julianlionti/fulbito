"""DT class"""
from dataclasses import dataclass
from common_attrs import CommonAttrs
from mentality import Mentality


@dataclass
class DT():
    """DT class"""
    attrs: CommonAttrs
    mentality: Mentality
