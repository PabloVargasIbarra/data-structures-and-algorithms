#Uses python3

import sys
import numpy as np


def edit_distance_three_sequences(s, t, r):
    len_s = len(s) + 1
    len_t = len(t) + 1
    len_r = len(r) + 1
    D = np.zeros((len_s, len_t, len_r), dtype=np.int8)
    for j in range(1, len_t):
        for i in range(1, len_s):
            for k in range(1, len_r):
                insertion_deletion = max(D[i-1, j, k], D[i, j-1, k], D[i, j, k - 1])
                if s[i-1] == t[j-1] == r[k-1]:
                    match = D[i-1, j-1, k-1] + 1
                    min_dist = max(insertion_deletion, match)
                else:
                    min_dist = max(insertion_deletion, D[i-1, j-1, k-1])
                D[i, j, k] = min_dist
    return D[len_s-1, len_t-1, len_r-1]


def lcs3(a, b, c):

    return edit_distance_three_sequences(a, b, c)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
