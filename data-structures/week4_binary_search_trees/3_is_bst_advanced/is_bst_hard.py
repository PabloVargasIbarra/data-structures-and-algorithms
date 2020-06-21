#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Tree:

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

    def is_binary_tree(self, tree_root, parent_key, parent_type):
        if self.n == 0:
            return True
        if tree_root == -1:
            return True
        if self.left[tree_root] != -1 and self.key[self.left[tree_root]] >= self.key[tree_root]:
            return False
        if self.right[tree_root] != -1 and self.key[self.right[tree_root]] < self.key[tree_root]:
            return False
        if self.right[tree_root] != -1 and parent_type == 'left' and self.key[self.right[tree_root]] >= parent_key:
            return False
        if self.left[tree_root] != -1 and parent_type == 'right' and self.key[self.left[tree_root]] < parent_key:
            return False
        return (self.is_binary_tree(self.left[tree_root], self.key[tree_root], parent_type='left')
                and self.is_binary_tree(self.right[tree_root], self.key[tree_root], parent_type='right'))


def main():
    tree = Tree()
    is_binary = tree.is_binary_tree(0, -1, 'none')
    if is_binary:
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

