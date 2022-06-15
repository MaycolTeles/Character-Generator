"""
Module containing the 'CharacterController' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.App.app import App
    from src.Models.Archetype.archetype import Archetype
    from src.Models.Race.race import Race

# MODULE IMPORTS
from src.Interfaces.MVC.View.UI_interface import UI
from src.Interfaces.MVC.Model.database_interface import Database

from src.TEMP.archetypes import AVAILABLE_ARCHETYPES
from src.TEMP.races import AVAILABLE_RACES

from src.Models.Character.character import Character


class CharacterController():
    """
    Class containing all the character controller responsabilities, like:

    # TODO: CREATE DOCSTRING
    """

    def __init__(
        self,
        model: Database,
        view: UI,
        app: App
    ) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.model = model
        self.view = view
        self.app = app

    def create_character(self) -> Character:
        """
        TODO: CREATE DOCSTRING
        """
        archetype = self.choose_archetype()
        race = self.choose_race()
        name = self.choose_name()

        return Character(
            archetype=archetype,
            race=race,
            name=name
        )

    def save_character_in_database(self) -> bool:
        """
        TODO: CREATE DOCSTRING
        """
        character = self.create_character()
        return self.model.insert_character(character)

    def load_character_from_database(self) -> Character:
        """
        TODO: CREATE DOCSTRING
        """
        self.view.show_message('Loading character...')
        character_name = self.view.get_input('Enter your character Name: ').title()

        character = self.model.read_character(character_name)

        if not character:
            self.view.show_message(
                f'Impossible to load the character {character_name}. '
                'The character was not found!')
            return False

        return character

    def update_character_in_database(self) -> Character:
        """
        TODO: CREATE DOCSTRING
        """
        self.view.show_message('Updating character...')
        character_name = self.view.get_input('Enter your character Name: ').title()

        character = self.model.read_character(character_name)

        if not character:
            self.view.show_message(
                f'Impossible to load the character {character_name}. '
                'The character was not found!')
            return False

        return character

    def delete_character_in_database(self) -> bool:
        """
        # TODO: CREATE DOCSTRING
        """
        self.view.show_message('Deleting character...')
        character_name = self.view.get_input('Enter your character Name: ').title()

        character = self.model.delete_character(character_name)

        if not character:
            self.view.show_message(
                f'Impossible to delete the character {character_name}. '
                'The character was not found!')
            return False

        return character

    def choose_archetype(self) -> Archetype:
        """
        TODO: CREATE DOCSTRING
        """
        character_archetype = self.view.get_input(
            'Enter your character Archetype (Class): ').lower()

        while character_archetype not in AVAILABLE_ARCHETYPES:
            character_archetype = self.view.get_input(
                'Enter your character Archetype (Class): '
            ).lower()

        archetype = AVAILABLE_ARCHETYPES[character_archetype]

        return archetype()

    def choose_race(self) -> Race:
        """
        TODO: CREATE DOCSTRING
        """
        character_race = None

        while character_race not in AVAILABLE_RACES:
            character_race = self.view.get_input(
                'Enter your character Race: '
            ).lower()

        race = AVAILABLE_RACES[character_race]

        return race()

    def choose_name(self) -> str:
        """
        TODO: CREATE DOCSTRING
        """
        character_name = self.view.get_input('Enter your character Name: ').title()

        return character_name
