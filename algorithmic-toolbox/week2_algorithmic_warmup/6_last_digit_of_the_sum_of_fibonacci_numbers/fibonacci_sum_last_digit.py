# Uses python3
import sys


# def get_fibonacci_last_digit(n):
#     if n <= 1:
#         return n
#     previous = 0
#     current = 1
#     for _ in range(n - 1):
#         previous, current = current, (previous + current) % 10
#
#     return current
#
#
# def get_pisano_mod_10():
#     pisano = [0, 1]
#     for i in range(2, 1000):  # maximum iterations
#         pisano.append(get_fibonacci_last_digit(i))
#         if pisano[(i - 1):(i + 1)] == [0, 1]:
#             return pisano[:-2]


def fibonacci_sum_last_digit(n):
    if n <= 1:
        return n

    pisano_mod10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9,
                    8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    return sum(pisano_mod10[:(n % len(pisano_mod10) + 1)]) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))
