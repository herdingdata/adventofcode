import unittest

from advent2017.day09.stream_processor import score_groups


class TestStreamProcessor(unittest.TestCase):
    def test_score_group_example_case_1_scores_1(self):
        input_text = '{}'
        expected = 1
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_2_scores_6(self):
        input_text = '{{{}}}'
        expected = 6
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_3_scores_5(self):
        input_text = '{{},{}}'
        expected = 5
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_4_scores_16(self):
        input_text = '{{{},{},{{}}}}'
        expected = 16
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_5_scores_1(self):
        input_text = '{<a>,<a>,<a>,<a>}'
        expected = 1
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_6_scores_9(self):
        input_text = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
        expected = 9
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_7_scores_9(self):
        input_text = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
        expected = 9
        result = score_groups(input_text)
        self.assertEqual(result, expected)

    def test_score_group_example_case_8_scores_3(self):
        input_text = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
        expected = 3
        result = score_groups(input_text)
        self.assertEqual(result, expected)