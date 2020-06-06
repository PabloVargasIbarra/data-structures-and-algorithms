# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def parent(i):
    return int(i/2)


def left_child(i):
    return 2 * (i + 1) - 1


def right_child(i):
    return 2 * (i + 1)


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def sift_down(heap_times, heap_workers, i):
    min_index = i
    size = len(heap_times)
    l = left_child(i)
    r = right_child(i)
    if r < size and heap_times[r] == heap_times[l] and heap_times[r] < heap_times[i]:
        if heap_workers[l] < heap_workers[r]:
            min_index = l
        else:
            min_index = r
    else:
        if l < size and heap_times[l] < heap_times[min_index]:
            min_index = l
        if r < size and heap_times[r] < heap_times[min_index]:
            min_index = r
    if min_index != i:
        swap(heap_times, i, min_index)
        swap(heap_workers, i, min_index)
        sift_down(heap_times, heap_workers, min_index)


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    next_worker = list(range(n_workers))
    for job in jobs:
        result.append(AssignedJob(next_worker[0], next_free_time[0]))
        next_free_time[0] += job
        sift_down(next_free_time, next_worker, 0)
    return result


# def stress_test():
#     import numpy as np
#     n_iter = 100000
#     for _ in range(n_iter):
#         n_workers = np.random.randint(1, 100)
#         n_jobs = [0] * n_workers # np.random.randint(0, 0, n_workers)
#         correct_solution = assign_jobs_naive(n_workers, n_jobs)
#         tentative_solution = assign_jobs(n_workers, n_jobs)
#         if tentative_solution != correct_solution:
#             print(f'Correct: {correct_solution}')
#             print(f'Tentative: {tentative_solution}')
#             print(n_workers)
#             print(n_jobs)
#             break


def main():
    # stress_test()
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
