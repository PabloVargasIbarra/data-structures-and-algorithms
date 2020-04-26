# Uses python3
import sys


def calc_fib(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % m

    return current


def get_pisano_mod(m):
    pisano = [0, 1]
    for i in range(2, 100000):  # maximum iterations
        pisano.append(calc_fib(i, m))
        if pisano[(i - 1):(i + 1)] == [0, 1]:
            return pisano[:-2]


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    pisano = get_pisano_mod(m)
    return pisano[n % len(pisano)]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
