"""
Module containing the 'MySQL' Class.
"""

# TYPING IMPORTS
from mysql.connector import MySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor

from typing import Any, List

# MODULE IMPORTS
import mysql.connector as mysql

from src.Env.variables import HOST, USER, PASSWORD, DATABASE
from src.Interfaces.MVC.Model.database_interface import Database
from src.Models.Character.character import Character


QUERY_PATH = 'App/database/queries/'


class MySQL(Database):
    """
    Class to represent a MySQL Database.

    This class implements the 'Database' Interface,
    so it must implement all the 'Database' functionalities, like:
    
    - Handling database queries.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    __database_connection: MySQLConnection
    __cursor: CMySQLCursor

    def __connect(self) -> bool:
        """
        Method to connect to the database.

        Returns
        --------
        bool
            - True if connection was successfully established;
            - False otherwise.
        """
        try:
            self.__database_connection = mysql.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DATABASE
            )
            self.__cursor = self.__database_connection.cursor()

        except mysql.Error as error:
            print('ERROR!')
            print(f'Error while trying to connect to the database: {error}')
            return False

        return True

    def __close(self) -> bool:
        """
        Method to close the connection to the database.

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """
        try:
            self.__cursor.close()
            self.__database_connection.close()

        except mysql.Error as error:
            print('ERROR!')
            print(f'Error while closing connection to the database: {error}')
            return False

        return True

    def __execute_query(self, query: str, params: List[Any] = []) -> Any:
        """
        Method to execute the query received as argument with the parameters
        (If any - The default is an empty list for select's, for example)
        received as argument.

        Parameters
        -----------
        query : str
            The query to be executed.

        params : List[Any], optional
            The parameters to be used in the query.
            The default value is an empty list.

        Returns
        --------
        Any
            - The data if the query was successafully executed;
            - False otherwise.
        """
        res = False

        try:
            self.__connect()
            self.__cursor.execute(query, params)
            res = self.__cursor.fetchall()
            self.__database_connection.commit()

        except mysql.Error as error:
            print('ERROR!')
            print(f'Error while trying to insert data into the database: {error}')

        finally:
            self.__close()

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
        try:
            with open(QUERY_PATH + 'insert_character.sql', 'r') as file:
                query = file.read()
                self.__execute_query(query, character.params_to_database())

        except Exception as error:
            print('ERROR!')
            print(f'Error while trying to insert the character into the database: {error}')
            return False

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
        bool
            - True if data was successfully updated;
            - False otherwise.
        """
        try:
            with open(QUERY_PATH + 'read_character.sql', 'r') as file:
                query = file.read()
                character = self.__execute_query(query, [character_name])

        except Exception as error:
            print('ERROR!')
            print(f'Error while trying to read the character from the database: {error}')
            return False


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
        try:
            with open(QUERY_PATH + 'delete_character.sql', 'r') as file:
                query = file.read()
                self.__execute_query(query, [character_name])

        except Exception as error:
            print('ERROR!')
            print(f'Error while trying to delete the character from the database: {error}')
            return False

        return True
