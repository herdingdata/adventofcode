from dataclasses import dataclass
from typing import Tuple

import numpy as np


def adjacent_array(array: np.array, start_xy: Tuple[int, int], end_xy: Tuple[int, int]) -> np.array:
    """
    Selects all adjacent cells surrounding the xy position, where (0, 0) xy is top left
    Consider this array:
    ```
    00000000
    00111100
    00199100
    00111100
    00000000
    ```
    if we give start xy as () and end xy as () i.e. the position of the 99
    then what will be returned is an array of all the 1s and 9s, omitting the 0s
    """
    min_x = max(0, start_xy[0] - 1)
    min_y = max(0, start_xy[1] - 1)
    max_x = min(array.shape[1], end_xy[0] + 1)
    max_y = min(array.shape[0], start_xy[1] + 1)
    array_incl_adjacents = array[min_y:max_y + 1, min_x:max_x + 1]
    return array_incl_adjacents


@dataclass
class PossiblePartNumber:
    value: int
    start_xy: Tuple[int, int]
    end_xy: Tuple[int, int]
    _is_real_part: bool = None
    _is_gear_part: bool = None

    def is_real_part(self, entire_symbol_array: np.array) -> bool:
        # pt1 - is it a legitimate part i.e. does it have a symbol adjacent
        if self._is_real_part is None:
            adjacents_issymbols = adjacent_array(entire_symbol_array, self.start_xy, self.end_xy)
            self._is_real_part = adjacents_issymbols.any()
        return self._is_real_part


class EngineSchematic:
    # Representation of the grid that we get from our puzzle input
    schematic_str: str          # the exact puzzle input
    schematic_array: np.array   # np array representation of puzzle input
    is_sym_arr: np.array           # array of true/false for whether it's a symbol or not
    is_num_arr: np.array           # array of true/false for whether it's a numvber or not
    is_ast_arr: np.array           # array of true/false for whether it's a numvber or not
    _all_part_numbers: list[PossiblePartNumber] = None
    _all_actual_part_numbers: list[PossiblePartNumber] = None

    def __init__(self, puzzle_input: str):
        self.schematic_str = puzzle_input
        self.schematic_array = np.array([list(row) for row in puzzle_input[:-1].split('\n')])

        # np array of true/falses, true where element is a symbol:
        is_symbol = np.vectorize(lambda x: not x.isnumeric() and x != '.')
        self.is_sym_arr = is_symbol(self.schematic_array)

        # np array of true/falses, true where element is a numeric digit:
        is_num = np.vectorize(lambda x: x.isnumeric())
        self.is_num_arr = is_num(self.schematic_array)

        # np array of true/falses, true where element is *:
        is_asterix = np.vectorize(lambda x: x == "*")
        self.is_ast_arr = is_asterix(self.schematic_array)

    @property
    def all_possible_part_numbers(self) -> list[int]:
        # all numbers from the schematic, regardless of whether or not they're a valid part
        if self._all_part_numbers is None:
            # if I was really smart I would have thought to use numpy _before_ I implemented this bit
            # maybe future me will make this better by numpy-ing it
            nums = []
            current_num_str = ''
            start_xy = None
            end_xy = None
            current_x_pos = -1  # root is top left of diagram
            current_y_pos = 0
            for character in self.schematic_str:
                if character == "\n":
                    current_y_pos += 1
                    current_x_pos = -1
                    continue  # we don't need to do anything with this character so go to the next one
                current_x_pos += 1

                # figure out what to do with it
                if character.isnumeric():
                    if current_num_str == '':
                        # we've found the start of a new number
                        current_num_str = character
                        start_xy = (current_x_pos, current_y_pos)
                        end_xy = (current_x_pos, current_y_pos)
                    else:
                        # we've found the continuation of a number
                        current_num_str += character
                        end_xy = (current_x_pos, current_y_pos)
                else:
                    if len(current_num_str) > 0:
                        # we've reached the end of a number
                        if start_xy is None:
                            raise ValueError(f"Part {current_num_str} has a (0,0) start position")
                        if end_xy is None:
                            raise ValueError(f"Part {current_num_str} has a (0,0) end position")
                        nums.append(PossiblePartNumber(value=int(current_num_str), start_xy=start_xy, end_xy=end_xy))
                        current_num_str = ''
                        start_xy = None
                        end_xy = None
            self._all_part_numbers = nums
        return [x.value for x in self._all_part_numbers]

    @property
    def all_possible_parts(self) -> list[PossiblePartNumber]:
        # same as all_possible_part_numbers except it returns the instances of PossiblePartNumbers
        if self._all_part_numbers is None:
            _ = self.all_possible_part_numbers
        return self._all_part_numbers

    @property
    def all_actual_parts(self) -> list[PossiblePartNumber]:
        if self._all_actual_part_numbers is None:
            actual_parts = []
            for part in self.all_possible_parts:
                if part.is_real_part(self.is_sym_arr):
                    actual_parts.append(part)
            self._all_actual_part_numbers = actual_parts
        return self._all_actual_part_numbers


if __name__ == "__main__":
    puzzle = open('puzzle_input.txt').read()
    schematic = EngineSchematic(puzzle)
    actual_parts = schematic.all_actual_parts
    print(f"sum of all actual parts is {sum([x.value for x in actual_parts])}")  # 535235
