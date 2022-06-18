"""
Module containing the 'Race' Abstract Class.
"""

from abc import ABC
from dataclasses import dataclass


@dataclass
class Race(ABC):
    """
    Class to represent a generic Race.
    """
