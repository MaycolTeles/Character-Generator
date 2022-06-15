"""
Module containing the 'MySQL' Class.
"""

# TYPE ANNOTATIONS IMPORTS
from mysql.connector import MySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor

from typing import Any, List, Optional, Union

# MODULE IMPORTS
import mysql.connector as mysql

from contextlib import contextmanager

from src.Env.variables import HOST, USER, PASSWORD, DATABASE
from src.Exceptions.character_not_found import CharacterNotFoundException
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

        cursor: CMySQLCursor = connection.cursor()

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

        with connect() as cursor:
            cursor.execute(query, params)

            res = cursor.fetchall()

        print(res)

        return res

    def build_character(self, character_data: List[str]) -> Character:
        """
        Method to build a character according to the data
        retrieved from the database.

        Returns
        --------
        Character
            The built character.
        """
        return Character(
            name=character_data[0],
            archetype=character_data[1],
            race=character_data[2],
            level=character_data[3]
        )

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
        with open(self.QUERY_PATH + 'insert_character.sql', 'r') as file:
            query = file.read()
            self.__execute_query(query, character.params_to_database())

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
        CharacterNotFoundException
            If the character was not found in the database.
        """
        with open(self.QUERY_PATH + 'read_character.sql', 'r') as file:
            query = file.read()
            character = self.__execute_query(query, [character_name])

        if not character:
            raise CharacterNotFoundException(
                'Character not found in the database.'
            )

        return character

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
            - False otherwise.
        """
        with open(self.QUERY_PATH + 'delete_character.sql', 'r') as file:
            query = file.read()
            self.__execute_query(query, [character_name])

        return True
