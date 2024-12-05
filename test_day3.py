import unittest
from src.day3 import main_a, main_b

class Day1Test(unittest.TestCase):
    def test_main_a(self):
        test_cases = [
            ("inputs_2024/day_3a_small.txt", 161),
            ("inputs_2024/day_3a_large.txt", 182619815)
        ]
        for filepath, expected_result in test_cases:
            result = main_a(filepath)
            self.assertEqual(result, expected_result)

    def test_main_b(self):
        test_cases = [
            ("inputs_2024/day_3b_small.txt", 48),
            ("inputs_2024/day_3b_large.txt", 80747545)
        ]
        for filepath, expected_result in test_cases:
            result = main_b(filepath)
            self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()