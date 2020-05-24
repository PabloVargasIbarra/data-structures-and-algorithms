#python3
import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def push(self, a):
        if self.__max_stack and a < self.__max_stack[-1]:
            self.__max_stack.append(self.__max_stack[-1])
        else:
            self.__max_stack.append(a)
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__max_stack.pop()

    def max_value(self):
        assert(len(self.__max_stack))
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max_value())
        else:
            assert False
