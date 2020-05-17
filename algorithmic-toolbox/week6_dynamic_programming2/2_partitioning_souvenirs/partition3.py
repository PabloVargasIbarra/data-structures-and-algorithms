# Uses python3
import sys
import numpy as np


# def partition3_brute_force(A):
#     import itertools
#     for c in itertools.product(range(3), repeat=len(A)):
#         sums = [None] * 3
#         for i in range(3):
#             sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
#
#         if sums[0] == sums[1] and sums[1] == sums[2]:
#             return 1
#
#     return 0


def partition3(elements):
    """Reference: https://web.cs.ucdavis.edu/~amenta/w04/dis4.pdf"""
    n_elements = len(elements)
    sum_elements = sum(elements)
    if n_elements < 3 or sum_elements % 3:
        return 0
    division_value = sum_elements // 3
    matrix = np.zeros((division_value + 1, division_value + 1, n_elements + 1), dtype=np.bool)
    matrix[0, 0, 0] = 1
    for element_idx in range(0, n_elements):
        for value_x in range(0, division_value + 1):
            for value_y in range(0, division_value + 1):
                k = elements[element_idx]
                is_partition = matrix[value_x, value_y, element_idx]
                if value_x >= k:
                    is_partition = is_partition or matrix[value_x-k, value_y, element_idx]
                if value_y >= k:
                    is_partition = is_partition or matrix[value_x, value_y-k, element_idx]
                matrix[value_x, value_y, element_idx+1] = is_partition
    return int(matrix[division_value, division_value, n_elements])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
