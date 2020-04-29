# python3
import sys


def compute_min_refills(distance, tank, stops):
    current_position = 0
    n_stops = 0
    while current_position + tank < distance:
        stops_candidates = [stop for stop in stops if current_position < stop <= current_position + tank]
        if len(stops_candidates) == 0:
            return -1
        else:
            current_position = max(stops_candidates)
            n_stops += 1
    return n_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
