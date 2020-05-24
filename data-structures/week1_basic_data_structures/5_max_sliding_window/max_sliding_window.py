# python3
from math import ceil


class StackWithMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, a):
        if self.max_stack and a < self.max_stack[-1]:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(a)
        self.stack.append(a)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.max_stack.pop()

    def max_value(self):
        if not self.max_stack:
            return -1
        return self.max_stack[-1]

    def extend(self, l):
        for a in l:
            self.push(a)


def max_sliding_window_naive(sequence, m):
    maximums = []
    n_windows = len(sequence) - m + 1
    n_partitions = ceil(n_windows / m)
    for p in range(n_partitions):
        p0 = p * m
        p1 = p0 + m
        stack_left, stack_right = StackWithMax(), StackWithMax()
        partition = sequence[p0:p1]
        stack_left.extend(reversed(partition))
        for j in range(min(m, n_windows - p0)):
            maximums.append(max(stack_left.max_value(), stack_right.max_value()))
            stack_left.pop()
            if p1+j < len(sequence):
                stack_right.push(sequence[p1+j])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

