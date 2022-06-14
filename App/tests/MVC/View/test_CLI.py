"""
Module containing the 'TestCLI' Class.
"""

import io
import unittest
from unittest.mock import patch, MagicMock

from src.MVC.View.CLI import CLI


class TestCLI(unittest.TestCase):
    """
    Class containing all the tests for the 'CLI' class.
    """

    def setUp(self) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        self.CLI_instance = CLI()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show(self, mock_stdout: io.StringIO) -> None:
        """
        TODO: CREATE DOCSTRING.
        """
        message = 'test'
        self.CLI_instance.show(message)

        actual = message + '\n'
        expected = mock_stdout.getvalue()

        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='test')
    def test_get_input(self, mock_input: MagicMock) -> None:
        """
        TODO: CREATE DOCSTRING
        """
        actual = self.CLI_instance.get_input()
        expected = mock_input.return_value

        self.assertEqual(actual, expected)
