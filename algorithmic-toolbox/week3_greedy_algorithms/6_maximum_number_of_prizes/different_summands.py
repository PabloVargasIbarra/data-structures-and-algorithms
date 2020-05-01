# Uses python3
import sys


def optimal_summands(n):
    summands = []
    current_summand = 1
    while (n - current_summand) > current_summand:
        summands.append(current_summand)
        n -= current_summand
        current_summand += 1
    summands.append(n)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
