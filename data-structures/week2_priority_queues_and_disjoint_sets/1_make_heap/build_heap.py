# python3


def parent(i):
    return int(i/2)


def left_child(i):
    return 2 * (i + 1) - 1


def right_child(i):
    return 2 * (i + 1)


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def sift_down(heap, i, swaps):
    min_index = i
    size = len(heap)
    l = left_child(i)
    if l < size and heap[l] < heap[min_index]:
        min_index = l
    r = right_child(i)
    if r < size and heap[r] < heap[min_index]:
        min_index = r
    if min_index != i:
        swaps.append((i, min_index))
        swap(heap, i, min_index)
        sift_down(heap, min_index, swaps)


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)
    for i in range(int(n / 2), -1, -1):
        sift_down(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
