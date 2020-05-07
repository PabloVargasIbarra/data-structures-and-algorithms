#Uses python3
import sys
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def minimum_distance(x, y):
    sorted_points = [(xi, yi) for xi, yi in sorted(zip(x, y))]
    return calculate_minimum_distance(sorted_points)


def calculate_minimum_distance(points):
    N = len(points)
    if N <= 3:
        d = float('inf')
        for i in range(N-1):
            for j in range(i+1, N):
                d_candidate = distance(points[i], points[j])
                if d_candidate < d:
                    d = d_candidate
        return d
    med = N // 2
    d1 = calculate_minimum_distance(points[:med])
    d2 = calculate_minimum_distance(points[med:])
    d = min(d1, d2)
    remaining_points = [(xi, yi) for xi, yi in points
                        if abs(xi - points[med][0]) < d]
    remaining_points = sorted(remaining_points, key=lambda p: p[1])
    # |i - j| > 7
    for i in range(len(remaining_points) - 1):
        for j in range(i+1, min(len(remaining_points), i+8)):
            d_candidate = distance(remaining_points[i], remaining_points[j])
            if d_candidate < d:
                d = d_candidate
    return d


def brute_force(points):
    N = len(points)
    d = float('inf')
    for i in range(N - 1):
        for j in range(i+1, N):
            d_candidate = distance(points[i], points[j])
            if d_candidate < d:
                d = d_candidate
    return d


def stress_test():
    import numpy
    flag_correct = True
    i = 0
    N = 4
    while flag_correct:
        x = numpy.random.randint(0, 3, size=N)
        y = numpy.random.randint(0, 3, size=N)
        points = [(xi, yi) for (xi, yi) in zip(x, y)]
        print(N, points)

        fast = minimum_distance(x, y)
        brute = brute_force(points)

        if fast != brute:
            print('Naive algorithm:', brute)
            print('Fast algorithm:', fast)
            flag_correct = False

        i += 1


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
