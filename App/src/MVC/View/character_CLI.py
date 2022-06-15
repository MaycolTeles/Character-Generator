"""
Module containing the 'CLI' Class.
"""

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

    def show_archetype_options(self) -> None:
        """
        Method to show the menu to the user.
        """
        self.show_message('''
        Please, choose an option from the archetypes below:
        
        1 - Bandit
        2 - Prophet
        3 - Samurai
        4 - Exit
        ''')
