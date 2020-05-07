# Uses python3
import sys


# slower implementation
# def fast_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     segments_sorted = [(end, start) for end, start in sorted(zip(ends, starts))]
#     ends = [s[0] for s in segments_sorted]
#     starts = [s[1] for s in segments_sorted]
#     points_sorted = sorted((p, i) for i, p in enumerate(points))
#     for p, i in points_sorted:
#         segment_idx = 0
#         flag_check = True
#         while flag_check and segment_idx < len(starts):
#             if p > ends[segment_idx]:
#                 ends.pop(segment_idx)
#                 starts.pop(segment_idx)
#             elif p >= starts[segment_idx]:
#                 cnt[i] += 1
#                 segment_idx += 1
#             else:
#                 flag_check = False
#     return cnt


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_num = [i for _, i in sorted(zip(points, range(len(points))))]

    # 0 - starts; 1 - points; 2 - ends
    full_points = [(p, 1) for p in points]
    full_points.extend([(s, 0) for s in starts])
    full_points.extend([(e, 2) for e in ends])

    full_points.sort()

    num_open_segments = 0
    i = 0
    for val, p_type in full_points:
        if p_type == 0:
            num_open_segments += 1
        elif p_type == 2:
            num_open_segments -= 1
        else:
            cnt[points_num[i]] = num_open_segments
            i += 1
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
