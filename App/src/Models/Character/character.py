"""
Module containing the 'Character' Abstract Class.
"""

from abc import ABC
from dataclasses import dataclass

from src.Models.Archetype.archetype import Archetype
from src.Models.Race.race import Race


@dataclass
class Character(ABC):
    """
    Class to represent a generic character.
    """

    name: str
    archetype: Archetype
    race: Race
    level: int

    def __init__(
        self,
        name: str,
        archetype: Archetype,
        race: Race,
        level: int=0
    ) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.name = name
        self.archetype = archetype
        self.race = race
        self.level = level

    def params_to_database(self):
        """
        TODO: CREATE DOCSTRING
        """
        return [
            self.name,
            self.archetype.__class__.__name__,
            self.race.__class__.__name__,
            self.level
        ]
