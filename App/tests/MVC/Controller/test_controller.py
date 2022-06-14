"""
Module containing the 'TestController' Class.
"""

# MODULE IMPORTS
import unittest

from src.MVC.View.CLI import CLI
from src.MVC.Model.MySQL import MySQL

from src.MVC.Controller.controller import Controller
from src.Models.Character.character import Character
from src.Models.Archetype.archetype import Archetype
from src.Models.Race.race import Race


class TestController(unittest.TestCase):
    """
    Class containing test for the 'Controller' Class.
    """

    def setUp(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.controller_instance = Controller(
            model=MySQL(),
            view=CLI()
        )

    def test_create_character(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        character = self.controller_instance.create_character()

        self.assertIsInstance(character, Character)

    def test_choose_archetype(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        archetype = self.controller_instance.choose_archetype()

        self.assertIsInstance(archetype, Archetype)

    def test_choose_race(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        race = self.controller_instance.choose_race()

        self.assertIsInstance(race, Race)

    def test_choose_name(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        name = self.controller_instance.choose_name()

        self.assertEqual(name, 'Malygos')
