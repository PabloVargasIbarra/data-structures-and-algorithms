#Uses python3

import sys


def safe_a_greater_b(a, b):
    return str(a) + str(b) > str(b) + str(a)


def largest_number(digits):
    number = ''
    while digits:
        max_digit = 0
        for digit in digits:
            if safe_a_greater_b(digit, max_digit):
                max_digit = digit
        number += max_digit
        digits.remove(max_digit)
    return number


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
