import unittest
from day08.register_instructions import Registry

class TestRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = Registry()

    def test_update_registry_with_instruction_a_is_0_inc_not_applied(
            self):
        instruction = 'b inc 5 if a > 1'
        expected = ('b', 0)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_a_is_2_inc_is_applied(
            self):
        self.registry.set_item_value('a', 2)
        instruction = 'b inc 5 if a > 1'
        expected = ('b', 5)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_b_is_0_inc_is_applied(
            self):
        instruction = 'a inc 1 if b < 5'
        expected = ('a', 1)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_b_is_5_inc_not_applied(
            self):
        self.registry.set_item_value('b', 5)
        instruction = 'a inc 1 if b < 5'
        expected = ('a', 0)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_a_is_0_dec_not_applied(
            self):
        instruction = 'c dec -10 if a >= 1'
        expected = ('c', 0)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_a_is_1_dec_is_applied(
            self):
        self.registry.set_item_value('a', 5)
        instruction = 'c dec -10 if a >= 1'
        expected = ('c', 10)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_c_is_10_inc_is_applied(
            self):
        self.registry.set_item_value('c', 10)
        instruction = 'c inc -20 if c == 10'
        expected = ('c', -10)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_update_registry_with_instruction_c_is_0_inc_not_applied(
            self):
        instruction = 'c inc -20 if c == 10'
        expected = ('c', 0)
        result = self.registry.update_registry_with_instruction(instruction)
        self.assertEqual(result, expected)

    def test_get_largest_value_in_registry_after_some_instructions_retusrns1(
            self):
        self.registry.update_registry_with_instruction('b inc 5 if a > 1')
        self.registry.update_registry_with_instruction('a inc 1 if b < 5')
        self.registry.update_registry_with_instruction('c dec -10 if a >= 1')
        self.registry.update_registry_with_instruction('c inc -20 if c == 10')
        self.assertEqual(self.registry.get_largest_value_in_registry(), 1)