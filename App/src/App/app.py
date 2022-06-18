"""
Module containing the 'App' Class.
"""

import os

from src.MVC.Model.MySQL import mysql_instance

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
            model=mysql_instance,
            view=GeneralCLI(),
            app=self
        )

        self.character_controller = CharacterController(
            model=mysql_instance,
            view=CharacterCLI(),
        )

        self.__setup()

    def __setup(self) -> None:
        """
        Method to setup the application
        """
        # CLEAR THE TERMINAL
        os.system('cls||clear')

    def run(self) -> None:
        """
        Method to run the application
        """
        self.general_controller.run()
