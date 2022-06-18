"""
Module containing the 'Database' Interface.
"""

from typing import Protocol, Any, List


class Database(Protocol):
    """
    Interface to represent a Database.

    This Interface contains all the 'Database' functionalities, like:
    
    - Handling database queries.

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def __connect(self) -> bool:
        """
        Method to connect to the database.

        This method must be implemented in all classes that
        implements this interface.

        Returns
        --------
        bool
            - True if connection was successfully established;
            - False otherwise.
        """

    def __close(self) -> bool:
        """
        Method to close the connection to the database.

        This method must be implemented in all classes that
        implements this interface

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """

    def __execute_query(self, query: str, params: List[Any] = []) -> bool:
        """
        Method to insert some data into the database.

        This method must be implemented in all classes that
        implements this interface

        Returns
        --------
        bool
            - True if data was successfully inserted into the database;
            - False otherwise.
        """
