"""
Module containing the 'CLI' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from typing import Optional

# MODULE IMPORTS
from abc import ABC

from src.Interfaces.MVC.View.UI_interface import UI


class CLI(ABC, UI):
    """
    Abstract Class to represent a Command Line Interface.

    This class implements the 'UI' Interface, so
    it has all the 'UI' functionalities, like:

    - Reading user inputs.
    - Showing some informations for the user.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def show_message(self, msg: str) -> None:
        """
        Method to show some message to the user.

        Parameters
        -----------
        msg : str
            The message to be printed to the user.
        """
        print(msg)

    def show_error(self, error: str) -> None:
        """
        Method to show the error to the user.

        Parameters
        -----------
        error : str
            The error to be printed to the user.
        """
        self.show_message(f'''
        Error: {error}''')

    def show_error_option_invalid(self, option: str) -> None:
        """
        Method to show the error to the user.

        Parameters
        -----------
        option : str
            The option that the user typed.
        """
        self.show_message(f'''
        Error: '{option}' isn't a valid option! Please, try again.''')

    def get_input(
        self,
        msg: Optional[str]='Please, choose one option: '
    ) -> str:
        """
        Method to get some input from the user.

        Parameters
        -----------
        msg : str, optional
            The message to be printed to the user.
            This parameters is optional.
            If it's not passed, its default value will be:
            'Digite a opção desejada: '

        Returns
        --------
        str
            The user input.
        """
        return input(msg).title().strip()

    def get_option(self) -> str:
        """
        Method to get the user input from the menu.

        Returns
        --------
        str
            The user input.
        """
        return self.get_input('\nType your option: ')
