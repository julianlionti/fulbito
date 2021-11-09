"""Locality class"""
from dataclasses import dataclass
from enum import Enum


@dataclass
class Locality(Enum):
    """Locality attrs"""
    LOCAL = 0
    VISITOR = 1
