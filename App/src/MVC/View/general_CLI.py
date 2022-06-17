"""
Module containing the 'CLI' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from typing import Dict

# MODULE IMPORTS
from src.MVC.View.CLI import CLI


class GeneralCLI(CLI):
    """
    Class to represent a general CLI.

    This class implements the 'UI' Interface, so
    it has all the 'UI' functionalities, like:

    - Reading user inputs.
    - Showing some informations for the user.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def show_menu_options(self, menu_options: Dict[str, str]) -> None:
        """
        Method to show the menu to the user.

        Parameters
        ----------
        menu_options : Dict[str, Dict]
            Dict containing the menu options.
        """
        self.show_message('''
        Please, choose an option from the menu below:
        ''')

        for option, description in menu_options.items():
            self.show_message(f'\t{option} - {description}')

    def get_menu_option(self) -> str:
        """
        Method to get the user input from the menu.

        Returns
        -----------
        str
            The user input.
        """
        return self.get_input('''
        Type your option: '''
        )
