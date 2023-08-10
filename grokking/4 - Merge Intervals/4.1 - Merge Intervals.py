# Given a list of intervals, merge all the overlapping intervals to produce a list
# that has only mutually exclusive intervals.

# Example 1:
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap,
# we merged them into one [1,5].

# Example 2:
# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap,
# we merged them into one [5,9].

# Example 3:
# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[", str(self.start), ", ", str(self.end), "]", end="")


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals


def main():
    print("Merged intervals: ", end="")
    for interval in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        interval.print_interval()
    print()

    print("Merged intervals: ", end="")
    for interval in merge([Interval(1, 7), Interval(2, 4), Interval(5, 9)]):
        interval.print_interval()
    print()

    print("Merged intervals: ", end="")
    for interval in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        interval.print_interval()
    print()


main()
