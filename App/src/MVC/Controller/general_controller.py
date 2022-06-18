"""
Module containing the 'GeneralController' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.App.app import App
    from src.MVC.View.CLI import CLI
    from src.Interfaces.MVC.Model.database_interface import Database

# MODULE IMPORTS
import sys


class GeneralController():
    """
    Class containing all the general controller responsabilities, like:

    - Calling the view to get input from the user
    - Calling the model to store general data
    """

    def __init__(self, model: Database, view: CLI, app: App) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.model = model
        self.view = view
        self.app = app

    def run(self) -> None:
        """
        Method to run the application
        """
        self.view.show_message('''
            Welcome to the Character Creator!
        ''')

        while True:
            self.menu()

    def exit(self) -> None:
        """
        Method to exit the application
        """
        self.view.show_message('\nThank you for using our application!\n')
        sys.exit()

    def menu(self) -> None:
        """
        Method to show the menu and execute the selected option.
        """
        AVAILABLE_MENU_FUNCTIONS = {
            '1': self.app.character_controller.save_character_in_database,
            '2': self.app.character_controller.load_character_from_database,
            '3': self.app.character_controller.load_all_characters_from_database,
            '4': self.app.character_controller.update_character_in_database,
            '5': self.app.character_controller.delete_character_in_database,
            '6': self.exit
        }

        AVAILABLE_MENU_OPTIONS = {
            '1': 'Save a character in the database',
            '2': 'Load a character from the database',
            '3': 'Load all characters from the database',
            '4': 'Update a character in the database',
            '5': 'Delete a character in the database',
            '6': 'Exit'
        }

        self.view.show_menu_options(AVAILABLE_MENU_OPTIONS)

        menu_option = self.view.get_menu_option()

        while menu_option not in AVAILABLE_MENU_FUNCTIONS:
            self.view.show_error_option_invalid(menu_option)
            menu_option = self.view.get_menu_option()

        # EXECUTING THE SELECTED OPTION
        AVAILABLE_MENU_FUNCTIONS[menu_option]()
