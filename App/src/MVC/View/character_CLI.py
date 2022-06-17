"""
Module containing the 'CLI' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from typing import Dict, List
from src.Models.Character.character import Character
from src.Models.Archetype.archetype import Archetype
from src.Models.Race.race import Race

# MODULE IMPORTS
from src.MVC.View.CLI import CLI


class CharacterCLI(CLI):
    """
    Class to represent a Command Line Interface.

    This class implements the 'UI' Interface, so
    it has all the 'UI' functionalities, like:

    - Reading user inputs.
    - Showing some informations for the user.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def show_archetypes_options(self, archetypes: Dict[str, Archetype]) -> None:
        """
        Method to show all the available archetypes to the user.

        Parameters
        ----------
        archetypes : Dict[str, Archetype]
            Dictionary where the keys are all the available archetypes.
        """
        self.show_message('''
        Please, choose an Archetype for your character '''
        '''from the list of available Archetypes below:''')

        for archetype in archetypes:
            self.show_message(f'''
            -> {archetype}''')

    def get_archetype_option(self) -> str:
        """
        Method to get the user choosen archetype.

        Returns
        -------
        str
            The user choosen archetype.
        """
        return self.get_input('''
        Choose your character's archetype: ''')

    def show_races_options(self, races: Dict[str, Race]) -> None:
        """
        Method to show all the available races to the user.

        Parameters
        ----------
        races : Dict[str, Races]
            Dictionary where the keys are all the available races.
        """
        self.show_message('''
        Please, choose a Race for your character '''
        '''from the list of available Races below:''')

        for race in races:
            self.show_message(f'''
            -> {race}''')

    def get_race_option(self) -> str:
        """
        Method to get the user choosen race.

        Returns
        -------
        str
            The user choosen race.
        """
        return self.get_input("\n\tChoose your character's Race: ")

    def get_character_name(self) -> str:
        """
        Method to get the character name.

        Returns
        -------
        str
            The character name.
        """
        return input('''
        Please, enter your character name: ''')

    def show_character(self, character: Character) -> None:
        """
        Method to show the character.
        """
        for attribute, value in character.get_attributes().items():
            self.show_message(f'\t-> {attribute.title()}: {value}')

    def show_characters(self, characters: List[Character]) -> None:
        """
        Method to show a list of characters.
        """
        for idx, character in enumerate(characters):
            self.show_message(f'\n\t**** Character {idx + 1} ****\n')

            for attribute, value in character.get_attributes().items():
                self.show_message(f'\t-> {attribute.title()}: {value}')

    def show_error_character_not_found(self, character_name: str) -> None:
        """
        Method to show the error to the user.

        Parameters
        ----------
        character_name : str
            The character name.
        """
        self.show_message(f'''
        Error! The Character '{character_name}' was not found in the database!''')

        self.show_message('''
        Please check if the name is correct or try to add a new character.''')

    def show_error_no_character_found(self) -> None:
        """
        Method to show the error to the user.
        """
        self.show_message('''
        Error! There are no characters in the database!''')

        self.show_message('''
        Please try to add a new character before searching for any.''')
