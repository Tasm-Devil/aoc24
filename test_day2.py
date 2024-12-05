import unittest
from src.day2 import main_a, main_b

class Day1Test(unittest.TestCase):
    def test_main_a(self):
        test_cases = [
            ("inputs_2024/day_2_small.txt", 2),
            ("inputs_2024/day_2_large.txt", 236)
        ]
        for filepath, expected_result in test_cases:
            result = main_a(filepath)
            self.assertEqual(result, expected_result)

    def test_main_b(self):
        test_cases = [
            ("inputs_2024/day_2_small.txt", 4),
            ("inputs_2024/day_2_large.txt", 308)
        ]
        for filepath, expected_result in test_cases:
            result = main_b(filepath)
            self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()