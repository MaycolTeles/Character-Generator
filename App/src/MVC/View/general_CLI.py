"""
Module containing the 'CLI' Class.
"""

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

    def show_menu_options(self) -> None:
        """
        Method to show the menu to the user.
        """
        self.show_message('''
        Please, choose an option from the menu below:
        
        1 - Create a new character
        2 - Load character
        3 - Update character
        4 - Delete character
        5 - Exit''')

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