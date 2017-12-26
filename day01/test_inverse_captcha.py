import unittest
from inverse_captcha import get_captcha


class TestInverseCaptcha(unittest.TestCase):
    def test_1122(self):
        start_num = 1122
        expected = 3
        result = get_captcha(start_num)
        self.assertEqual(expected, result)

    def test_1111(self):
        start_num = 1111
        expected = 4
        result = get_captcha(start_num)
        self.assertEqual(expected, result)

    def test_1234(self):
        start_num = 1234
        expected = 0
        result = get_captcha(start_num)
        self.assertEqual(expected, result)

    def test_91212129(self):
        start_num = 91212129
        expected = 9
        result = get_captcha(start_num)
        self.assertEqual(expected, result)
