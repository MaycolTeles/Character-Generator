"""
Main module containing the start of your application.
"""

from src.App.app import App


def main() -> None:
    """
    Main function. This is where your application will start.
    """

    app = App()

    app.run()


# def test():
#     from src.Models.Character.character import Character
#     from src.Entities.Archetypes.bandit import Bandit
#     from src.Entities.Races.dwarf import Dwarf
#     character = Character('sda', Bandit(), Dwarf(), 1)

#     values = character.get_attributes()

#     print(values)


if __name__ == '__main__':
    main()
