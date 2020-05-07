# Uses python3
import sys


def merge(arr, l, m, r):
    number_of_inversions = 0
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            number_of_inversions += len(L[i:])
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

        # Copy the remaining elements of R[], if there
        # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return number_of_inversions


def get_number_of_inversions(arr, l, r):
    number_of_inversions = 0
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        number_of_inversions += get_number_of_inversions(arr, l, m)
        number_of_inversions += get_number_of_inversions(arr, m + 1, r)
        number_of_inversions += merge(arr, l, m, r)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a) - 1))
