from typing import List
from itertools import islice

from helpers import read


def count_increments(depth_readings: list) -> int:
    # pt1
    increments = 0
    for idx, reading in enumerate(depth_readings):
        if idx > 0: # we don't have a previous reading
            if reading > last_reading:
                increments += 1
        last_reading = reading
    return increments


def get_sum_of_3_readings(depth_readings: List[int], start: 0) -> int:
    return sum(islice(depth_readings, start, start + 3))


def count_increments_across_3_readings(depth_readings: List[int]) -> int:
    # pt2
    increments = 0
    for idx, reading in enumerate(depth_readings):
        depth = get_sum_of_3_readings(depth_readings, idx)
        if idx > 0: # we don't have a previous reading
            if depth > last_reading:
                increments += 1
        last_reading = depth
    return increments



if __name__ == "__main__":
    #pt1
    depths = [int(x) for x in read.read_file_as_list('y2021/day01/puzzle_input.txt')]
    print(count_increments(depths))

    #pt2
    depths = [int(x) for x in read.read_file_as_list('y2021/day01/puzzle_input.txt')]
    print(count_increments_across_3_readings(depths))
