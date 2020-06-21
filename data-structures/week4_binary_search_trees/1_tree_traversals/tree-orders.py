# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def __init__(self):
        # read
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        self.in_order = self._in_order(0)
        self.pre_order = self._pre_order(0)
        self.post_order = self._post_order(0)

    def _in_order(self, tree_root):
        if tree_root == 0:
            self.result = []
        if tree_root == -1:
            return
        self._in_order(self.left[tree_root])
        self.result.append(self.key[tree_root])
        self._in_order(self.right[tree_root])
        return self.result

    def _pre_order(self, tree_root):
        if tree_root == 0:
            self.result = []
        if tree_root == -1:
            return
        self.result.append(self.key[tree_root])
        self._pre_order(self.left[tree_root])
        self._pre_order(self.right[tree_root])
        return self.result

    def _post_order(self, tree_root):
        if tree_root == 0:
            self.result = []
        if tree_root == -1:
            return
        self._post_order(self.left[tree_root])
        self._post_order(self.right[tree_root])
        self.result.append(self.key[tree_root])
        return self.result


def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.in_order))
    print(" ".join(str(x) for x in tree.pre_order))
    print(" ".join(str(x) for x in tree.post_order))


threading.Thread(target=main).start()
