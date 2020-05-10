#Uses python3

import sys
import numpy as np


def edit_distance(s, t, match_reward, insertion_deletion_cost, mismatch_cost):
    len_s = len(s) + 1
    len_t = len(t) + 1
    D = np.zeros((len_s, len_t), dtype=np.int8)
    D[0, :] = [insertion_deletion_cost] * len_t
    D[:, 0] = [insertion_deletion_cost] * len_s
    for j in range(1, len_t):
        for i in range(1, len_s):
            insertion = D[i, j-1] + insertion_deletion_cost
            deletion = D[i-1, j] + insertion_deletion_cost
            if s[i-1] == t[j-1]:
                match = D[i-1, j-1] + match_reward
                min_dist = max(insertion, deletion, match)
            else:
                mismatch = D[i-1, j-1] + mismatch_cost
                min_dist = max(insertion, deletion, mismatch)
            D[i, j] = min_dist
    return D[len_s-1, len_t-1]


def lcs2(a, b):

    return edit_distance(a, b, 1, 0, 0)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
