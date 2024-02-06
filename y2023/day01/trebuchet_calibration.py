from helpers import read

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}
LEN_OF_TEXT_DIGITS = set([len(s) for s in DIGITS.keys()])


def _get_first_digit(sample: str):
    for char in sample:
        if char.isnumeric():
            return char


def _get_last_digit(sample: str):
    for char in sample[::-1]:
        if char.isnumeric():
            return char


def _get_first_text_number(sample):
    for start_pos in range(0, len(sample)):
        for len_of_text in LEN_OF_TEXT_DIGITS:
            evaluate_text = sample[start_pos:start_pos+len_of_text]
            if evaluate_text in DIGITS:
                return DIGITS[evaluate_text]


def _get_last_text_number(sample):
    for start_pos in reversed(range(0, len(sample))):
        for len_of_text in LEN_OF_TEXT_DIGITS:  # this could be more efficient
            evaluate_text = sample[start_pos:start_pos+len_of_text]
            if evaluate_text in DIGITS:
                return DIGITS[evaluate_text]


def get_calibration_value_pt1(sample: str):
    return int(_get_first_digit(sample) + _get_last_digit(sample))


def get_calibration_value_pt2(sample: str):
    return int(_get_first_text_number(sample) + _get_last_text_number(sample))


def main():
    samples = read.read_file_as_list('y2023/day01/puzzle_input.txt')

    # pt1
    running_total = 0
    for calib_val in samples:
        running_total += get_calibration_value_pt1(calib_val)
    print(f"part1:{running_total}")

    # pt2
    running_total2 = 0
    for calib_val in samples:
        running_total2 += get_calibration_value_pt2(calib_val)
    print(f"part1:{running_total2}")



if __name__ == "__main__":
    main()
