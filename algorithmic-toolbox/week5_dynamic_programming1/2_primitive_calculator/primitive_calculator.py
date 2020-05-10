# Uses python3
import sys


def optimal_sequence(n):
    intermediate_numbers = [[]] * max(4, (n + 1))
    intermediate_numbers[1] = [1]
    intermediate_numbers[2] = [1, 2]
    intermediate_numbers[3] = [1, 3]
    for number in range(4, n + 1):
        # sum
        sum_min = len(intermediate_numbers[number - 1]) + 1
        # multiplication 2
        rest_2 = number % 2
        mul2_min = len(intermediate_numbers[number // 2]) + rest_2
        # multiplication 3
        rest_3 = number % 3
        mul3_min = len(intermediate_numbers[number // 3]) + rest_3
        # global minimum
        global_min = min(sum_min, mul2_min, mul3_min)
        if global_min == sum_min:
            intermediate_numbers[number] = intermediate_numbers[number - 1] + [number]
        elif global_min == mul2_min:
            intermediate_numbers[number] = intermediate_numbers[number // 2] + [number - rest_2 + i
                                                                                for i in range(rest_2 + 1)]
        else:
            intermediate_numbers[number] = intermediate_numbers[number // 3] + [number - rest_3 + i
                                                                                for i in range(rest_3 + 1)]
    return intermediate_numbers[n]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
