# Uses python3
import sys
import numpy as np


def optimal_weight(W, w):
    n_w = W
    n_items = len(w)
    M = np.zeros((n_w + 1, n_items + 1), dtype=np.int64)
    for j in range(1, n_items + 1):
        for i in range(1, n_w + 1):
            M[i, j] = M[i, j-1]
            if i >= w[j-1]:
                val = M[i - w[j-1], j-1] + w[j-1]
                if M[i, j] < val:
                    M[i, j] = val
    return M[n_w, n_items]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
