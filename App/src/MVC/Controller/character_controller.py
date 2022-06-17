"""
Module containing the 'CharacterController' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.Models.Archetype.archetype import Archetype
    from src.Models.Race.race import Race

# MODULE IMPORTS
from src.TEMP.archetypes import AVAILABLE_ARCHETYPES
from src.TEMP.races import AVAILABLE_RACES

from src.Exceptions.character_not_found_in_database import CharacterNotFoundInDatabaseException
from src.Interfaces.MVC.View.UI_interface import UI
from src.Interfaces.MVC.Model.database_interface import Database

from src.Models.Character.character import Character


class CharacterController():
    """
    Class containing all the character controller responsabilities, like:

    # TODO: CREATE DOCSTRING
    """

    def __init__(self, model: Database, view: UI) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.model = model
        self.view = view

    def create_character(self) -> Character:
        """
        TODO: CREATE DOCSTRING
        """
        archetype = self.choose_archetype()
        race = self.choose_race()
        name = self.choose_name()

        character = Character(
            archetype=archetype,
            race=race,
            name=name
        )

        self.view.show_message('\n\t************************')
        self.view.show_message('\tCharacter created:')
        self.view.show_character(character)
        self.view.show_message('\t************************')

        return character

    def save_character_in_database(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        character = self.create_character()

        self.model.insert_character(character)

    def load_character_from_database(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        character_name = self.view.get_character_name()

        try:
            character = self.model.read_character(character_name)

        except CharacterNotFoundInDatabaseException:
            self.view.show_error_character_not_found(character_name)
            return

        else:
            self.view.show_character(character)

    def load_all_characters_from_database(self) -> None:
        """
        # TODO: CREATE DOCSTRING
        """
        try:
            characters = self.model.read_all_characters()

        except CharacterNotFoundInDatabaseException:
            self.view.show_error_no_character_found()
            return

        else:
            self.view.show_characters(characters)

    def update_character_in_database(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        character_name = self.view.get_character_name()

        try:
            character = self.model.read_character(character_name)
        
        except CharacterNotFoundInDatabaseException:
            self.view.show_error_character_not_found(character_name)
            return

        else:
            self.view.show_character(character)

    def delete_character_in_database(self) -> None:
        """
        # TODO: CREATE DOCSTRING
        """
        character_name = self.view.get_character_name()

        try:
            res = self.model.delete_character(character_name)

        except CharacterNotFoundInDatabaseException:
            self.view.show_error_character_not_found(character_name)
            return

        self.view.show_message('\n\tCharacter deleted.')

    def choose_archetype(self) -> Archetype:
        """
        TODO: CREATE DOCSTRING
        """
        # SHOWING AVAILABLE ARCHETYPES
        self.view.show_archetypes_options(AVAILABLE_ARCHETYPES)

        # GETTING THE ARCHETYPE
        archetype_option = self.view.get_archetype_option()

        # REPEAT THE LOOP IF THE USER INPUT ISN'T VALID
        while archetype_option not in AVAILABLE_ARCHETYPES:
            self.view.show_error_option_invalid(archetype_option)
            archetype_option = self.view.get_archetype_option()

        # RETURNING THE AVAILABLE ARCHETYPE OBJECT
        archetype_obj = AVAILABLE_ARCHETYPES[archetype_option]

        return archetype_obj()

    def choose_race(self) -> Race:
        """
        TODO: CREATE DOCSTRING
        """
        # SHOWING AVAILABLE RACES
        self.view.show_races_options(AVAILABLE_RACES)

        # GETTING THE RACE
        race_option = self.view.get_race_option()

        # REPEAT THE LOOP IF THE USER INPUT ISN'T VALID
        while race_option not in AVAILABLE_RACES:
            self.view.show_error_option_invalid(race_option)
            race_option = self.view.get_race_option()

        # RETURNING THE AVAILABLE ARCHETYPE OBJECT
        race = AVAILABLE_RACES[race_option]

        return race()

    def choose_name(self) -> str:
        """
        TODO: CREATE DOCSTRING
        """
        character_name = self.view.get_character_name()

        return character_name
