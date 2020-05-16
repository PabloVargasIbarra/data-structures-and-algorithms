# Uses python3
import numpy as np


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def calculate_max_min(M, m, i, j, ops):
    maximum = float('-inf')
    minimum = float('inf')
    for idx in range(j - i):
        min_op_max = evalt(m[i, i + idx], M[i + idx + 1, j], ops[i+idx])
        max_op_min = evalt(M[i, i + idx], m[i + idx + 1, j], ops[i+idx])
        min_op_min = evalt(m[i, i + idx], m[i + idx + 1, j], ops[i+idx])
        max_op_max = evalt(M[i, i + idx], M[i + idx + 1, j], ops[i+idx])
        maximum = max(maximum, min_op_max, max_op_min, min_op_min, max_op_max)
        minimum = min(minimum, min_op_max, max_op_min, min_op_min, max_op_max)
    return maximum, minimum


def get_maximum_value(dataset):
    ops = dataset[1::2]
    numbers = dataset[0::2]
    n_numbers = len(numbers)
    M = np.zeros((n_numbers, n_numbers), dtype=np.int64)
    m = np.zeros((n_numbers, n_numbers), dtype=np.int64)
    for i in range(n_numbers):
        M[i, i] = numbers[i]
        m[i, i] = numbers[i]
    for s in range(1, n_numbers):  # diagonal start column
        for j in range(s, n_numbers):
            i = j - s
            M[i, j], m[i, j] = calculate_max_min(M, m, i, j, ops)
    return M[0, n_numbers-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
