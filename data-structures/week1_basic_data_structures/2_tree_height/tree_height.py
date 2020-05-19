# python3

import sys
import threading


def create_tree(n, parents):
    root = None
    tree = [[] for _ in range(n)]
    for idx, parent in enumerate(parents):
        if parent == -1:
            root = idx
        else:
            tree[parent].append(idx)
    return root, tree


def compute_height_recursive(root, tree):
    stack_height = []
    if tree[root]:
        for node in tree[root]:
            stack_height.append(compute_height_recursive(root=node,
                                                         tree=tree) + 1)
        return max(stack_height)
    else:
        return 0


def compute_height(n, parents):
    root, tree = create_tree(n, parents)
    return compute_height_recursive(root, tree) + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
