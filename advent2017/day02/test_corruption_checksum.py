import unittest

from advent2017.day02.corruption_checksum import get_checksum


class TestCorruptionChecksum(unittest.TestCase):
    def setUp(self):
        self.row1 = [5, 1, 9, 5]
        self.row2 = [7, 5, 3]
        self.row3 = [2, 4, 6, 8]

    def test_max9_min1_produces_8(self):
        test_input = [self.row1]
        result = get_checksum(test_input)
        self.assertEqual(result, 8)

    def test_max7_min3_produces_4(self):
        test_input = [self.row2]
        result = get_checksum(test_input)
        self.assertEqual(result, 4)

    def test_max7_min3_produces_4(self):
        test_input = [self.row3]
        result = get_checksum(test_input)
        self.assertEqual(result, 6)

    def test_many_rows_are_added_together(self):
        test_input = [self.row1, self.row2, self.row3]
        result = get_checksum(test_input)
        self.assertEqual(result, 18)
