# python3


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]


def poly_hash(S, p, x):
    ans = 0
    for c in reversed(S):
        ans = (ans * x + ord(c)) % p
    return ans


def precompute_hashes(text, len_pattern, p, x):
    H = [None for _ in range(len(text) - len_pattern + 1)]
    initial_pos_char = len(text) - len_pattern
    S = text[initial_pos_char:]
    H[len(text) - len_pattern] = poly_hash(S, p, x)
    y = 1
    for i in range(len_pattern):
        y = (y * x) % p
    for i in range(len(text) - len_pattern-1, -1, -1):
        H[i] = (x * H[i+1] + ord(text[i]) - y * ord(text[i + len_pattern])) % p
    return H


def get_occurrences(pattern, text):
    p = 1000000007
    x = 263
    result = []
    len_pattern = len(pattern)
    phash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, len_pattern, p, x)
    for i in range(len(text) - len_pattern + 1):
        if phash != H[i]:
            continue
        if text[i:(i+len_pattern)] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

