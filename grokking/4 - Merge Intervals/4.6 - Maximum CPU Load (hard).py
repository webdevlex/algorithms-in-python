from heapq import *


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # Min heap based on job.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    # Sort the jobs by start time
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    min_heap = []

    for j in jobs:
        # Remove all the jobs that have ended
        while len(min_heap) > 0 and j.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)

        # Add the current job into min_heap
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load


def main():
    print("Maximum CPU load at any time:", end=" ")
    print(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]))

    print("Maximum CPU load at any time:", end=" ")
    print(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 5)]))

    print("Maximum CPU load at any time:", end=" ")
    print(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]))


main()
