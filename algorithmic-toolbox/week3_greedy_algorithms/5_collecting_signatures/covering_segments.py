# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments = [segment for _, segment in sorted(zip([s.end for s in segments], segments))]
    while len(segments) > 0:
        points.append(segments[0].end)
        segments = [segment for segment in segments if segment.start > segments[0].end]
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
