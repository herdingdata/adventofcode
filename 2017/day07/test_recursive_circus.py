import unittest
from day07.recursive_circus import get_name_of_bottom_program_from_data_list


class TestRecursiveCircus(unittest.TestCase):
    def test_get_name_of_bottom_program_example_returns_tknk(self):
        input_data = ["pbga (66)\n",
                      "xhth (57)\n",
                      "ebii (61)\n",
                      "havc (66)\n",
                      "ktlj (57)\n",
                      "fwft (72) -> ktlj, cntj, xhth\n",
                      "qoyq (66)\n",
                      "padx (45) -> pbga, havc, qoyq\n",
                      "tknk (41) -> ugml, padx, fwft\n",
                      "jptl (61)\n",
                      "ugml (68) -> gyxo, ebii, jptl\n",
                      "gyxo (61)\n",
                      "cntj (57)"]
        expected_program = 'tknk'
        result = get_name_of_bottom_program_from_data_list(input_data)
        self.assertEqual(result, expected_program)
