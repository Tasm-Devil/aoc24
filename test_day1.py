import unittest
from unittest import mock  # Hinzufügen dieses Imports
from src.day1 import read_file, main_a, main_b

class Day1Test(unittest.TestCase):
    def test_main_a_small(self):
        filepath = "inputs_2024/day_1_small.txt"
        result = 11
        with unittest.mock.patch('builtins.print') as mock_print:
            main_a(filepath)
            mock_print.assert_called_with(result)

    def test_main_a_large(self):
        filepath = "inputs_2024/day_1_large.txt"
        result = 2113135
        with unittest.mock.patch('builtins.print') as mock_print:
            main_a(filepath)
            mock_print.assert_called_with(result)

    def test_main_b_small(self):
        filepath = "inputs_2024/day_1_small.txt"
        result = 31
        with unittest.mock.patch('builtins.print') as mock_print:
            main_b(filepath)
            mock_print.assert_called_with(result)

    def test_main_b_Large(self):
        filepath = "inputs_2024/day_1_large.txt"
        result = 19097157
        with unittest.mock.patch('builtins.print') as mock_print:
            main_b(filepath)
            mock_print.assert_called_with(result)

if __name__ == "__main__":
    unittest.main()