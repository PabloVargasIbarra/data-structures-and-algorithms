# Uses python3
import sys
import numpy as np


def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_value = np.array(values) / np.array(weights)
    item_order = np.array(range(len(values)))[(-unit_value).argsort()]
    for index in item_order:
        item_weight = min(capacity, weights[index])
        value += item_weight * unit_value[index]
        capacity -= item_weight
        if capacity <= 0:
            return value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
