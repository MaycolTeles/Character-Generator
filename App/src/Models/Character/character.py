"""
Module containing the 'Character' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from typing import Optional, Any, Dict

# MODULE IMPORTS
from dataclasses import dataclass

from src.Models.Archetype.archetype import Archetype
from src.Models.Race.race import Race


@dataclass
class Character():
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
        level: Optional[int]=0
    ) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.name = name
        self.archetype = archetype
        self.race = race
        self.level = level

    def get_attributes(self) -> Dict[str, Any]:
        """
        Method to return a dict where the
        attribute description is the dict key
        and the value is the dict value.
        """
        attributes = self.__dict__.keys()
        values = [value if isinstance(value, int) or isinstance(value, str) \
            else value.__class__.__name__ for value in self.__dict__.values()]

        return {attribute: value for attribute, value in zip(attributes, values)}
