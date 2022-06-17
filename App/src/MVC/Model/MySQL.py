"""
Module containing the 'MySQL' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from mysql.connector import MySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor

from typing import Any, Tuple, List, Optional, Union

# MODULE IMPORTS
import mysql.connector as mysql

from contextlib import contextmanager

from src.Env.variables import HOST, USER, PASSWORD, DATABASE
from src.Exceptions.character_not_found_in_database import CharacterNotFoundInDatabaseException
from src.Interfaces.MVC.Model.database_interface import Database
from src.Models.Character.character import Character


@contextmanager
def connect():
    """
    Function to connect to the database.

    This function should be used as a context manager.
    """

    connection: MySQLConnection
    cursor: CMySQLCursor

    try:
        connection = mysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        cursor = connection.cursor()

        yield cursor

    except mysql.Error as error:
        print('ERROR!')
        print(error)

    finally:
        connection.commit()
        cursor.close()
        connection.close()


class MySQL(Database):
    """
    Class to represent a MySQL Database.

    This class implements the 'Database' Interface,
    so it must implement all the 'Database' functionalities, like:

    - Handling database queries.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    QUERY_PATH = 'App/database/queries/'

    def __execute_query(
        self,
        query: str,
        params: Optional[List[Union[str, int]]]=None
    ) -> Any:
        """
        Method to execute the query received as argument with the parameters
        (If any - The default is an empty list for select's, for example)
        received as argument.

        Parameters
        -----------
        query : str
            The query to be executed.

        params : List[str, int], optional
            The parameters to be used in the query.
            The default value is an empty list.

        Returns
        --------
        Any
            - The data if the query was successafully executed;
            - False otherwise.
        """
        if params is None:
            params = []

        res = None

        with connect() as cursor:
            cursor.execute(query, params)

            res = cursor.fetchall()

        return res

    def insert_character(self, character: Character) -> bool:
        """
        Method to read some data from the database.

        Parameters
        -----------
        character : Character
            The character to be stored in the database.

        Returns
        --------
        Any
            The data that was read.
        """
        with open(self.QUERY_PATH + 'insert_character.sql', 'r') as query_file:
            query = query_file.read()
            self.__execute_query(query, list(character.get_attributes().values()))

        return True

    def read_character(self, character_name: str) -> Character:
        """
        Method to update some data in the database.

        Parameters
        -----------
        character_name : str
            The character name to access the character inside the database.

        Returns
        --------
        character : Character
            The character that was read from the database.

        Raises
        -------
        CharacterNotFoundInDatabaseException
            If the character was not found in the database.
        """
        with open(self.QUERY_PATH + 'read_character.sql', 'r') as query_file:
            query = query_file.read()
            character_data = self.__execute_query(query, [character_name])

        if not character_data:
            raise CharacterNotFoundInDatabaseException()

        character = self.build_characters(character_data)[0]

        return character

    def read_all_characters(self) -> List[Character]:
        """
        Method to read all characters from the database.

        Returns
        --------
        character : Character
            A list containing all characters found in the database.

        Raises
        -------
        CharacterNotFoundInDatabaseException
            If no character was found in the database.
        """
        with open(self.QUERY_PATH + 'read_all_characters.sql', 'r') as query_file:
            query = query_file.read()
            characters_data = self.__execute_query(query)

        if not characters_data:
            raise CharacterNotFoundInDatabaseException()

        characters = self.build_characters(characters_data)

        return characters

    def delete_character(self, character_name: str) -> bool:
        """
        Method to delete some data from the database.

        Parameters
        -----------
        character_name : str
            The character name to access the character
            to be deleted in the database.

        Returns
        --------
        bool
            - True if character was successfully deleted;
            - Raises an exception otherwise.

        Raises
        -------
        CharacterNotFoundInDatabaseException
            If the character was not found in the database.
        """
        # CHECKING IF THE CHARACTER EXISTS IN THE DATABASE
        character_exists = self.check_if_character_in_database(character_name)

        if not character_exists:
            raise CharacterNotFoundInDatabaseException()

        # CHARACTER EXISTS, TRYING TO DELETE IT FROM THE DATABASE
        with open(self.QUERY_PATH + 'delete_character.sql', 'r') as query_file:
            query = query_file.read()
            self.__execute_query(query, [character_name])

        return True

    def check_if_character_in_database(self, character_name: str) -> bool:
        """
        Method to check if a character exists in the database.

        Parameters
        -----------
        character_name : str
            The character name to access the character
            to be checked in the database.

        Returns
        --------
        bool
            - True if character exists in the database;
            - False otherwise.
        """
        with open(self.QUERY_PATH + 'read_character_name.sql', 'r') as query_file:
            query = query_file.read()
            character_exists = self.__execute_query(query, [character_name])

        return bool(character_exists)

    def build_characters(
        self,
        characters_data: List[Tuple[Union[str, int]]]
        ) -> List[Character]:
        """
        Method to build a list of characters from the data received as argument.

        Parameters
        -----------
        characters_data : List[Tuple[Union[str, int]]]
            The data to be used to build the list of characters.

        Returns
        -------
        List[Character]
            The list of characters built from the data received as argument.
        """

        characters = []

        for character_data in characters_data:

            name, archetype, race, level = character_data

            character = Character(
                name=name,
                archetype=archetype,
                race=race,
                level=level
            )

            characters.append(character)

        return characters
