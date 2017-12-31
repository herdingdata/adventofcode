import re
from pprint import pprint as pp


class Tower:
    def __init__(self):
        self.programs = []
        self.edges = []  # [(base_program, top_program)]

    def add_program(self, program_name):
        if program_name not in self.programs:
            self.programs.append(program_name)

    def add_program_above_another(self, base_program, top_program):
        self.add_program(base_program)
        self.add_program(top_program)
        self.edges.append((base_program, top_program))

    def which_program_is_at_the_bottom(self):
        """
        making the massive assumption that everything is joined up in our tower,
        the program at the bottom won't be named as the 'top program' in any
        edges. So let's find which program doesn't have any top edges.

        If this were to be scaled up/ run more than once, some edge case
        handling would prooooooobably be a good idea.

        :return: str: program_name
        """
        for program_name in self.programs:
            edges_where_this_one_is_a_top = {base:top for base, top in
                                             self.edges if top == program_name}
            if len(edges_where_this_one_is_a_top) == 0:
                return program_name


def get_name_of_bottom_program_from_data_list(input_data):
    program_pattern = re.compile('[a-z]+')
    tower = Tower()
    for row in input_data:
        row = row.replace('\n', '')
        programs_in_row = re.findall(program_pattern, row)
        program_name = programs_in_row[0]
        tower.add_program(program_name)
        if len(programs_in_row) > 1:
            [tower.add_program_above_another(program_name, top_prog) for
             top_prog in programs_in_row[1:]]
    return tower.which_program_is_at_the_bottom()

if __name__ == '__main__':
    input_data = open('puzzle_input.txt').readlines()
    result = get_name_of_bottom_program_from_data_list(input_data)
    pp('result: ' + str(result))