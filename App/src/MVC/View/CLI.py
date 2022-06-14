"""
Module containing the 'CLI' Class.
"""

from src.Interfaces.MVC.View.UI_interface import UI


class CLI(UI):
    """
    Class to represent a Command Line Interface.

    This class implements the 'UI' Interface, so
    it has all the 'UI' functionalities, like:
    
    - Reading user inputs.
    - Showing some informations for the user.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def show(self, msg: str) -> None:
        """
        Method to show some message or text to the user.

        Parameters
        -----------
        msg : str
            The message to be printed to the user.
        """
        print(msg)

    def get_input(self, msg: str='Digite a opção desejada: ') -> str:
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
        -----------
        str
            The user input.
        """
        return input(msg)
