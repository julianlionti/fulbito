"""Referee class"""
from dataclasses import dataclass
from common_attrs import CommonAttrs


@dataclass
class Referee():
    attrs: CommonAttrs
    experience: int


# atributos ocultos, corrupcion
