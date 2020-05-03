# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    duplicated = []
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            if a[i] == x:
                duplicated.append(j+1)
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    position_left = j
    for d in duplicated:
        flag_left = True
        while flag_left and position_left > d:
            position_left -= 1
            if a[position_left] < x:
                a[position_left], a[d] = a[d], a[position_left]
                flag_left = False
    return position_left, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


def stress_test():
    import numpy
    flag_correct = True
    i = 0
    while flag_correct:
        N = numpy.random.randint(1, 20)
        a = numpy.random.randint(0, 20, size=N)
        l = list(a).copy()
        print(N, a, i)

        alg_naive = sorted(l)
        randomized_quick_sort(l, 0, N-1)

        if alg_naive != l:
            print('Naive algorithm:', alg_naive)
            print('Fast algorithm:', l)
            flag_correct = False

        i += 1


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
