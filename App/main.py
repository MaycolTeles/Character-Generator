"""
Main module containing the start of your application.
"""

from src.MVC.View.CLI import CLI
from src.MVC.Model.MySQL import MySQL
from src.MVC.Controller.controller import Controller


def main() -> None:
    """
    Main function. This is where your application will start.
    """
    
    view = CLI()
    model = MySQL()
    controller = Controller(model, view)

    controller.save_character()

    char = controller.load_character()

    print(char)

    controller.delete_character()


def teste():
    """
    Test function.
    """
    pass


if __name__ == '__main__':
    main()
