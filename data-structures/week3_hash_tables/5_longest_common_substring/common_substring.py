# python3

import sys
from collections import namedtuple
import numpy as np

Answer = namedtuple('answer_type', 'i j len')


def solve_naive(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i + l] == t[j:j + l]):
                    ans = Answer(i, j, l)
    return ans


def poly_hash(S, p, x):
    ans = 0
    for c in reversed(S):
        ans = (ans * x + ord(c)) % p
    return ans


def precompute_hashes(text, len_pattern, p, x):
    H = [None for _ in range(len(text) - len_pattern + 1)]
    initial_pos_char = len(text) - len_pattern
    S = text[initial_pos_char:]
    H[len(text) - len_pattern] = poly_hash(S, p, x)
    H_set = {H[len(text) - len_pattern]}
    y = 1
    for i in range(len_pattern):
        y = (y * x) % p
    for i in range(len(text) - len_pattern - 1, -1, -1):
        H[i] = ((x * H[i + 1]) % p + ord(text[i]) - y * ord(text[i + len_pattern])) % p
        H_set.add(H[i])
    return H, H_set


def solve(s, t):
    ans = Answer(0, 0, 0)
    reverse = False
    if len(s) > len(t):
        reverse = True
        s, t = t, s
    larger_k = min(len(s), len(t)) + 1
    lower_k = 0
    mid_k = (larger_k + lower_k) // 2
    hash_condition = False
    p1 = 1000000007
    p2 = 1000004249
    x1 = np.random.randint(p1)
    x2 = np.random.randint(p2)
    while mid_k > ans.len:
        if larger_k <= ans.len:
            return ans
        Hs_1, Hs_1_set = precompute_hashes(s, mid_k, p1, x1)
        Ht_1, Ht_1_set = precompute_hashes(t, mid_k, p1, x1)
        Hs_2, Hs_2_set = precompute_hashes(s, mid_k, p2, x2)
        Ht_2, Ht_2_set = precompute_hashes(t, mid_k, p2, x2)
        for i in range(len(Hs_1)):
            if hash_condition:
                break
            if Hs_1[i] in Ht_1_set and Hs_2[i] in Ht_2_set:
                for j in range(len(Ht_1)):
                    # print(i,j)
                    hash_condition = Hs_1[i] == Ht_1[j] and Hs_2[i] == Ht_2[j]
                    if hash_condition:
                        # print(True)
                        if reverse:
                            ans = Answer(j, i, mid_k)
                        else:
                            ans = Answer(i, j, mid_k)
                        break
        if hash_condition:
            lower_k = mid_k
            hash_condition = False
        else:
            larger_k = mid_k
        mid_k = (larger_k + lower_k) // 2
    return ans


def stress_test():
    import random
    n_iter = 10000
    for _ in range(n_iter):
        n1 = 100
        n2 = 20
        s = ''.join(random.choice('abc') for _ in range(n1))
        t = ''.join(random.choice('abc') for _ in range(n2))
        naive = solve_naive(s, t)
        result = solve(s, t)
        if result.len != naive.len:
            print(s, t)
            print(result)
            print(naive)


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)

# if __name__ == '__main__':
#     stress_test()
