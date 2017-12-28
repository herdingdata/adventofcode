import unittest
from day05.twisty_trampolines import get_number_of_steps_to_exit_list

class TestTwistyTrampolines(unittest.TestCase):
    def test_number_of_steps_for_example_returns_5(self):
        input_list = [0, 3, 0, 1, -3]
        expected_steps = 5
        result = get_number_of_steps_to_exit_list(input_list)
        self.assertEqual(result, expected_steps)