import unittest

from advent2017.day01.inverse_captcha import get_captcha


class TestInverseCaptcha(unittest.TestCase):
    def test_two_groups_of_two_numbers_sum_one_of_each_digit(self):
        start_num = 1122
        expected = 3
        result = get_captcha(start_num)
        self.assertEqual(expected, result)

    def test_consecutive_digits_sum_all_digits(self):
        start_num = 1111
        expected = 4
        result = get_captcha(start_num)
        self.assertEqual(expected, result)

    def test_incrementing_numbers_sum_to_zero(self):
        start_num = 1234
        expected = 0
        result = get_captcha(start_num)
        self.assertEqual(expected, result)

    def test_first_and_last_digit_are_9_returns_9(self):
        start_num = 91212129
        expected = 9
        result = get_captcha(start_num)
        self.assertEqual(expected, result)
