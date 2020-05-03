# Uses python3
import sys
from numpy import random


def get_majority_element_naive(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    for i in range(right):
        cur_elem = a[i]
        cnt = 0
        for j in range(right):
            if a[j] == cur_elem:
                cnt += 1
        if cnt > right/2:
            return cur_elem
    return -1


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    sorted_list = sorted(a[left:right])
    value, count, max_count = sorted_list[0], 0, -1
    for i in sorted_list:
        count += 1
        if i != value:
            count = 1
            value = i
        if count > max_count:
            max_count = count
            max_value = i
    if max_count > (right - left) / 2:
        return max_value
    return -1


def get_majority_element_div_conq(a, left, right):
    if (right - left) == 1:
        return a[left]
    else:
        mid = (left + right) // 2
        left_maj_elem = get_majority_element(a, left, mid + 1)
        right_maj_elem = get_majority_element(a, mid, right)
        majority_elements = (e for e in (left_maj_elem, right_maj_elem) if e != -1)
        for number in majority_elements:
            count = 0
            for i in range(left, right):
                if a[i] == number:
                    count = count + 1
            if count > (right - left) / 2:
                return number
    return -1


def stress_test():
    flag_correct = True
    i = 0
    while flag_correct:
        N = random.randint(1, 10)
        a = random.randint(0, 10, size=N)
        a.sort()

        print(N, a, i)

        alg_naive = get_majority_element_naive(a, 0, N)
        alg_fast = get_majority_element_div_conq(a, 0, N)

        if alg_naive != alg_fast:
            print('Naive algorithm:', alg_naive)
            print('Fast algorithm:', alg_fast)
            flag_correct = False

        i += 1


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_div_conq(a, 0, n) != -1:
        print(1)
    else:
        print(0)
