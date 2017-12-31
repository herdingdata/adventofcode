from pprint import pprint as pp

def get_number_of_steps_to_exit_list(jump_list):
    """
    :param jump_list: list of ints
    :return: the number of steps to exit the jump list
    """
    steps = 0
    max_index = len(jump_list) - 1  # zero based
    end_has_been_reached = False
    current_index = 0
    while end_has_been_reached == False:
        # where will the jump take us?
        next_index = current_index + jump_list[current_index]
        jump_list[current_index] += 1
        # will the jump achieve our goal of escaping?
        steps += 1
        if next_index < 0 or next_index > max_index:
            end_has_been_reached = True
        # now do the jump
        current_index = next_index
    return steps


if __name__ == '__main__':
    input_list = open('puzzle_input.txt').readlines()
    input_list = [int(x.replace('\n', '')) for x in input_list]
    result = get_number_of_steps_to_exit_list(input_list)
    pp('result: ' + str(result))