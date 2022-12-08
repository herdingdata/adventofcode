from typing import List

from y2021.helpers import read


def pilot_the_sub(commands: List[str]) -> (int, int):
    pos_horiz = 0
    pos_depth = 0
    for command in commands:
        message, value_str = command.split(' ')
        value = int(value_str)
        if message == 'forward':
            pos_horiz += value
        elif message == 'down':
            pos_depth += value
        else:
            pos_depth -= value
    return pos_horiz, pos_depth


def pilot_with_aim(commands: List[str]) -> (int, int):
    pos_horiz = 0
    pos_depth = 0
    aim = 0
    for command in commands:
        message, value_str = command.split(' ')
        value = int(value_str)
        if message == 'forward':
            pos_horiz += value
            pos_depth += aim * value
        elif message == 'down':
            aim += value
        else:
            aim -= value
    return pos_horiz, pos_depth


if __name__ == "__main__":
    # pt1
    cmds = read.read_file_as_list('y2021/day02/puzzle_input.csv')
    horiz, depth = pilot_the_sub(cmds)
    print(f'{horiz=}, {depth=}, multiplied {horiz * depth}')

    # pt2
    horiz, depth = pilot_with_aim(cmds)
    print(f'{horiz=}, {depth=}, multiplied {horiz * depth}')
