import unittest

from advent2017.day04.high_entropy_passphrases import is_passphrase_valid


class TestHighEntropyPassphrases(unittest.TestCase):
    def test_simple_passphrase_is_valid(self):
        test_input = 'aa bb cc dd ee'
        expected = True
        result = is_passphrase_valid(test_input)
        self.assertEqual(result, expected)

    def test_repeated_word_not_valid(self):
        test_input = 'aa bb cc dd aa'
        expected = False
        result = is_passphrase_valid(test_input)
        self.assertEqual(result, expected)

    def test_similar_words_are_valid(self):
        test_input = 'aa bb cc dd aaa'
        expected = True
        result = is_passphrase_valid(test_input)
        self.assertEqual(result, expected)