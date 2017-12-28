import unittest
from day06.memory_reallocation import how_many_redistributions_until_repeat, \
    redistribute_memory_blocks


class TestHowManyRedistributionsUntilRepeat(unittest.TestCase):
    def test_how_many_redistributions_until_repeat_example_produces_5_cycles(
            self):
        memory_bank = [0, 2, 7, 0]
        expected_steps = 5
        result = how_many_redistributions_until_repeat(memory_bank)
        self.assertEqual(result, expected_steps)


class TestRedistributionCycle(unittest.TestCase):
    def test_redistribution_cycle_0270_produces_2412(self):
        input_memory_bank = [0, 2, 7, 0]
        expected_bank = [2, 4, 1, 2]
        result = redistribute_memory_blocks(input_memory_bank)
        self.assertEqual(result, expected_bank)

    def test_redistribution_cycle_2412_produces_3123(self):
        input_memory_bank = [2, 4, 1, 2]
        expected_bank = [3, 1, 2, 3]
        result = redistribute_memory_blocks(input_memory_bank)
        self.assertEqual(result, expected_bank)

    def test_redistribution_cycle_3123_produces_0234(self):
        input_memory_bank = [3, 1, 2, 3]
        expected_bank = [0, 2, 3, 4]
        result = redistribute_memory_blocks(input_memory_bank)
        self.assertEqual(result, expected_bank)

    def test_redistribution_cycle_0234_produces_1341(self):
        input_memory_bank = [0, 2, 3, 4]
        expected_bank = [1, 3, 4, 1]
        result = redistribute_memory_blocks(input_memory_bank)
        self.assertEqual(result, expected_bank)

    def test_redistribution_cycle_1341_produces_2412(self):
        input_memory_bank = [1, 3, 4, 1]
        expected_bank = [2, 4, 1, 2]
        result = redistribute_memory_blocks(input_memory_bank)
        self.assertEqual(result, expected_bank)