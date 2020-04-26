# Uses python3
import sys


def gcd(a, b):
    if b == 0:
        return a
    if b == 1:
        return b

    return gcd(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
