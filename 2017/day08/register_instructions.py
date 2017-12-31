import operator as op


class Registry:
    def __init__(self):
        self._dict = {}  # item name: value_as_integer
        self.condition_functions = {'>': op.gt,
                               '<': op.lt,
                               '>=': op.ge,
                               '<=': op.le,
                               '==': op.eq,
                               '!=': op.ne}
        self.action_functions = {'inc': op.add, 'dec': op.sub}

    def update_registry_with_instruction(self, instruction):
        """
        :param instruction: str: in the format "b inc 5 if a > 1"
        :return: (register_item_name_that_was_affected, value_after_instruction)
        """
        instruction_as_list = instruction.split(' ')
        register_item_name, inc_or_dec, value, _, condition_item_name, \
            condition, test_value = instruction_as_list
        value = int(value)
        test_value = int(test_value)
        existing_value = self.get_item_value(register_item_name)
        condition_existing_value = self.get_item_value(condition_item_name)
        condition_fn = self.condition_functions[condition]
        if condition_fn(condition_existing_value, test_value):
            new_value = self.action_functions[inc_or_dec](existing_value, value)
            self.set_item_value(register_item_name, new_value)
        return (register_item_name, self._dict[register_item_name])

    def get_largest_value_in_registry(self):
        max_found = None
        for k, v in self._dict.items():
            if max_found is None:
                max_found = v
            max_found = max(v, max_found)
        return max_found

    def set_item_value(self, item_name, new_value):
        self._dict[item_name] = new_value

    def get_item_value(self, item_name):
        self.add_item_to_register_if_necessary(item_name)
        return self._dict[item_name]

    def add_item_to_register_if_necessary(self, item_name):
        if item_name not in self._dict.keys():
            self._dict[item_name] = 0


def get_largest_value_from_register(instructions):
    """
    process all instructions then find the biggest value from the resulting
    register

    :param instructions: list of str: in the format "b inc 5 if a > 1"
    :return: int:
    """
    registry = Registry()
    for instruction in instructions:
        registry.update_registry_with_instruction(instruction.replace('\n', ''))
    return registry.get_largest_value_in_registry()


if __name__ == '__main__':
    instructions = open('instructions.txt').readlines()
    print(get_largest_value_from_register(instructions))