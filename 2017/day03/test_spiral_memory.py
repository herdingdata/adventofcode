import unittest
from day03.spiral_memory import get_distance


class TestSpiralMemory(unittest.TestCase):
    def test_input_one_produces_zero_steps(self):
        test_input = 1
        expected = 0
        result = get_distance(test_input)
        self.assertEqual(result, expected)

    def test_input_12_produces_3_steps(self):
        test_input = 12
        expected = 3
        result = get_distance(test_input)
        self.assertEqual(result, expected)

    def test_input_23_produces_2_steps(self):
        test_input = 23
        expected = 2
        result = get_distance(test_input)
        self.assertEqual(result, expected)

    def test_input_1024_produces_31_steps(self):
        test_input = 1024
        expected = 31
        result = get_distance(test_input)
        self.assertEqual(result, expected)
