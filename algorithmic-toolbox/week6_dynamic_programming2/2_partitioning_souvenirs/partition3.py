# Uses python3
import sys


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
    n_elements = len(elements)
    sum_elements = sum(elements)
    if n_elements < 3 or sum_elements % 3:
        return 0
    division_value = sum_elements // 3
    matrix = [[0] * (n_elements + 1) for _ in range(division_value + 1)]
    for value in range(1, division_value + 1):
        for element_last_idx in range(1, n_elements + 1):
            added_element = elements[element_last_idx-1]
            if added_element == value:
                matrix[value][element_last_idx] = min(matrix[value][element_last_idx-1] + 1, 2)
            elif value > added_element and matrix[value-added_element][element_last_idx-1]:
                matrix[value][element_last_idx] = min(matrix[value][element_last_idx - 1] + 1, 2)
            else:
                matrix[value][element_last_idx] = matrix[value][element_last_idx-1]
    return 1 if matrix[-1][-1] == 2 else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

