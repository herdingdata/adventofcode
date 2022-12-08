from typing import List

from y2021.helpers import read


def bin_to_dec(binary_value: str):
    return int(binary_value, 2)


def get_gamma_and_epsilon(binary_readings: List[str]) -> (int, int):
    gamma_bin = ''
    epsilon_bin = ''
    for idx in range(0, len(binary_readings[0])):  # assume they're all same len
        ones = sum([int(x[idx]) for x in binary_readings])
        zeroes = len([x[idx] for x in binary_readings if x[idx] == '0'])
        if ones > zeroes:
            gamma_bin += '1'
            epsilon_bin += '0'
        else:
            gamma_bin += '0'
            epsilon_bin += '1'
    gamma = bin_to_dec(gamma_bin)
    epsilon = bin_to_dec(epsilon_bin)
    return gamma, epsilon


def get_o2_generator(binary_readings: List[str]) -> (int, int):
    remaining_readings = binary_readings
    for idx in range(0, len(remaining_readings[0])):  # for each character, ignore the last one
        keep_these = []
        ones = sum([int(x[idx]) for x in remaining_readings])
        zeroes = len([x[idx] for x in remaining_readings if x[idx] == '0'])
        all_ones = [r for r in remaining_readings if r[idx] == '1']
        all_zeroes = [r for r in remaining_readings if r[idx] == '0']
        # for reading in remaining_readings:
        if ones == zeroes or ones > zeroes:
            keep_these.extend(all_ones)
        else:
            keep_these.extend(all_zeroes)
        if len(keep_these) == 1:
            return bin_to_dec(keep_these[-1])
        remaining_readings = keep_these
    return bin_to_dec(keep_these[-1])


def get_co2_scrubber(binary_readings: List[str]) -> int:
    remaining_readings = binary_readings
    for idx in range(0, len(remaining_readings[0])):  # for each character, ignore the last one
        keep_these = []
        ones = sum([int(x[idx]) for x in remaining_readings])
        zeroes = len([x[idx] for x in remaining_readings if x[idx] == '0'])
        all_ones = [r for r in remaining_readings if r[idx] == '1']
        all_zeroes = [r for r in remaining_readings if r[idx] == '0']
        # for reading in remaining_readings:
        if ones == zeroes or ones > zeroes:
            keep_these.extend(all_zeroes)
        else:
            keep_these.extend(all_ones)
        if len(keep_these) == 1:
            return bin_to_dec(keep_these[-1])
        remaining_readings = keep_these
    return bin_to_dec(keep_these[-1])


def get_life_support_rating(binary_readings: List[str]) -> int:
    o2 = get_o2_generator(binary_readings)
    co2 = get_co2_scrubber(binary_readings)
    return o2 * co2


if __name__ == "__main__":
    # pt1
    binary_readings = read.read_file_as_list('y2021/day03/puzzle_input.csv')
    gamma, epsilon = get_gamma_and_epsilon(binary_readings)
    print(f'{gamma=}, {epsilon=}, multiplied {gamma * epsilon}')

    # pt2
    print(get_life_support_rating(binary_readings))
