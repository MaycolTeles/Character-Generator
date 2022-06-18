"""
Module containing the 'TestMySQL' Class.
"""

import unittest

from src.MVC.Model.MySQL import MySQL


class TestMySQL(unittest.TestCase):
    """
    Class containing tests for the 'MySQL' class.
    """

    def setUp(self):
        """
        TODO: CREATE DOCSTRING
        """
        self.MySQL_instance = MySQL()

    def test_insert_data(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
