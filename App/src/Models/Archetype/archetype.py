"""
Module containing the 'Archetype' Abstract Class.
"""

from abc import ABC
from dataclasses import dataclass


@dataclass
class Archetype(ABC):
    """
    Class to represent a generic archetype (class).
    """
