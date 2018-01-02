import sys


def sum_digits_if_identical(digit_one, digit_two):
    result = 0
    if digit_one == digit_two:
        result = int(digit_one)
    return result


def get_captcha(input_num):
    total_sum = 0
    input_num_as_str = str(input_num)
    prev_digit = input_num_as_str[-1]  # start with the final digit
    for digit in input_num_as_str:
        total_sum += sum_digits_if_identical(digit, prev_digit)
        prev_digit = digit
    return total_sum


if __name__ == '__main__':
    print('captcha result: ' + str(get_captcha(sys.argv[1])))
