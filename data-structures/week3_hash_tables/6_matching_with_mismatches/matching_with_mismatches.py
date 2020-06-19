# python3

import sys
import numpy as np

# Failed case #5/7: time limit exceeded (Time used: 79.97/40.00, memory used: 26476544/536870912.)
# TODO: Implement a most efficient algorithm with running time O(nklog(n))


class HashEncoder:
    def __init__(self, s):
        self.s = s
        self.m1, self.m2 = 10 ** 9 + 7, 10 ** 9 + 9
        self.x1, self.x2 = np.random.randint(self.m1 - 1), np.random.randint(self.m2 - 1)
        self.h1, self.h2 = [0], [0]
        self.x1_pw = [1]
        self.x2_pw = [1]
        for i in range(1, len(self.s) + 1):
            self.x1_pw.append((self.x1_pw[i - 1] * self.x1) % self.m1)
            self.x2_pw.append((self.x2_pw[i - 1] * self.x2) % self.m2)
        for i in range(1, len(self.s) + 1):
            self.h1.append((self.x1 * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1)
            self.h2.append((self.x2 * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2)

    def hash(self, a, b):
        l = b - a + 1
        hash1 = (self.h1[a + l] - (self.x1_pw[l] * self.h1[a]) % self.m1) % self.m1
        hash2 = (self.h2[a + l] - (self.x2_pw[l] * self.h2[a]) % self.m2) % self.m2
        return hash1, hash2


def find_next_mismatch(text_encoded, pattern_encoded, a, b, i, min_dist, lst_mismatchs):
    # print(a, b, i)
    if len(lst_mismatchs) > min_dist:
        return
    # print(i + a, i + b)
    if b - a == 0:
        if text_encoded.hash(i + a, i + b) != pattern_encoded.hash(a, b):
            # print(i + a)
            lst_mismatchs.append(i + a)
        return
    # text_encoded.hash(i + a, i + b - a)
    # pattern_encoded.hash(a, b - a)
    if text_encoded.hash(i + a, i + b) != pattern_encoded.hash(a, b):
        # lst_mismatchs.append(i)
        med = (a + b) // 2
        find_next_mismatch(text_encoded, pattern_encoded, a, med, i, min_dist, lst_mismatchs)
        # if len(lst_mismatchs) > min_dist:
        #     return
        find_next_mismatch(text_encoded, pattern_encoded, med + 1, b, i, min_dist, lst_mismatchs)


def solve(k, text, pattern):
    result = []
    text_encoded = HashEncoder(text)
    pattern_encoded = HashEncoder(pattern)
    for i in range(len(text) - len(pattern) + 1):
        lst_mismatchs = []
        find_next_mismatch(text_encoded, pattern_encoded, 0, len(pattern) - 1, i, k, lst_mismatchs)
        # print(lst_mismatchs)
        if len(lst_mismatchs) <= k:
            result.append(i)
    return result


for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
