# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1, self.m2 = 10 ** 9 + 7, 10 ** 9 + 9
        self.x1, self.x2 = 1, 12  # random
        self.h1, self.h2 = [0], [0]
        self.x1_pw = [1]
        self.x2_pw = [1]
        for i in range(1, len(self.s)+1):
            self.x1_pw.append((self.x1_pw[i-1] * self.x1) % self.m1)
            self.x2_pw.append((self.x2_pw[i - 1] * self.x2) % self.m2)
        for i in range(1, len(self.s)+1):
            self.h1.append((self.x1 * self.h1[i - 1] + ord(self.s[i-1])) % self.m1)
            self.h2.append((self.x2 * self.h2[i - 1] + ord(self.s[i-1])) % self.m2)

    def ask(self, a, b, l):
        cond1 = (self.h1[a + l] - (self.x1_pw[l] * self.h1[a]) % self.m1) % self.m1 == (
                    self.h1[b + l] - (self.x1_pw[l] * self.h1[b]) % self.m1) % self.m1
        cond2 = (self.h2[a + l] - (self.x2_pw[l] * self.h2[a]) % self.m2) % self.m2 == (
                    self.h2[b + l] - (self.x2_pw[l] % self.m2 * self.h2[b]) % self.m2) % self.m2
        return cond1 and cond2


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
