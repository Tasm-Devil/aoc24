import unittest
from src.day1 import main_a, main_b

class Day1Test(unittest.TestCase):
    def test_main_a(self):
        test_cases = [
            ("inputs_2024/day_1_small.txt", 11),
            ("inputs_2024/day_1_large.txt", 2113135)
        ]
        for filepath, expected_result in test_cases:
            result = main_a(filepath)
            self.assertEqual(result, expected_result)

    def test_main_b(self):
        test_cases = [
            ("inputs_2024/day_1_small.txt", 31),
            ("inputs_2024/day_1_large.txt", 19097157)
        ]
        for filepath, expected_result in test_cases:
            result = main_b(filepath)
            self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()