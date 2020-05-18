# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_stack_position = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            opening_brackets_stack_position.append(i+1)
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            left_value = opening_brackets_stack.pop()
            opening_brackets_stack_position.pop()
            if not are_matching(left_value, next):
                return i + 1
    n_elements = len(opening_brackets_stack)
    return 'Success' if n_elements == 0 else opening_brackets_stack_position[-1]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
