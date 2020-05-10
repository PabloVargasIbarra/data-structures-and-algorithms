# Uses python3
import numpy as np


def edit_distance(s, t):
    len_s = len(s) + 1
    len_t = len(t) + 1
    D = np.zeros((len_s, len_t), dtype=np.int8)
    D[0, :] = range(len_t)
    D[:, 0] = range(len_s)
    for j in range(1, len_t):
        for i in range(1, len_s):
            insertion = D[i, j-1] + 1
            deletion = D[i-1, j] + 1
            if s[i-1] == t[j-1]:
                match = D[i-1, j-1]
                min_dist = min(insertion, deletion, match)
            else:
                mismatch = D[i-1, j-1] + 1
                min_dist = min(insertion, deletion, mismatch)
            D[i, j] = min_dist
    return D[len_s-1, len_t-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
