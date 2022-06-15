"""
Main module containing the start of your application.
"""

import os
from src.App.app import App


def main() -> None:
    """
    Main function. This is where your application will start.
    """

    # CLEAR THE TERMINAL
    os.system('cls||clear')

    app = App()

    app.run()


if __name__ == '__main__':
    main()
