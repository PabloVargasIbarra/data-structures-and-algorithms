# Uses python3
import sys


def get_change(m):
    n_coints = 0
    while m >= 10:
        n_coints += 1
        m -= 10
    while m >= 5:
        n_coints += 1
        m -= 5
    while m >= 1:
        n_coints += 1
        m -= 1
    return n_coints


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
