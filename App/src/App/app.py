"""
Module containing the 'App' Class.
"""

from src.MVC.Model.MySQL import MySQL

from src.MVC.View.general_CLI import GeneralCLI
from src.MVC.View.character_CLI import CharacterCLI

from src.MVC.Controller.general_controller import GeneralController
from src.MVC.Controller.character_controller import CharacterController


class App:
    """
    Class containing all the App functionalities.
    """

    def __init__(self) -> None:
        """
        # TODO: CREATE DOCSTRING
        """
        self.general_controller = GeneralController(
            model=MySQL(),
            view=GeneralCLI(),
            app=self
        )

        self.character_controller = CharacterController(
            model=MySQL(),
            view=CharacterCLI(),
            app=self
        )

    def run(self) -> None:
        """
        Method to run the application
        """
        self.general_controller.run()
