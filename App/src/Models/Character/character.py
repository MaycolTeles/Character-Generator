"""
Module containing the 'Character' Abstract Class.
"""

from abc import ABC

from src.Models.Archetype.archetype import Archetype
from src.Models.Race.race import Race


class Character(ABC):
    """
    Class to represent a generic character.
    """

    race: Race
    archetype: Archetype
    name: str
    level: int

    def __init__(
        self,
        race: Race,
        archetype: Archetype,
        name: str,
        level: int=0
    ) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.race = race
        self.archetype = archetype
        self.name = name
        self.level = level
