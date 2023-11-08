from typing import List, Optional


def merge_intervals(intervals: List[tuple[int, int]]) -> List[tuple[int, int]]:
    def _get_interval_start(val):
        return val[0]

    if not intervals:
        return []

    intervals.sort(key=_get_interval_start)
    result = []
    interval1 = intervals[0]
    for i in range(len(intervals)-1):
        merged_interval = _merge_interval(interval1, intervals[i+1])
        if merged_interval:
            interval1 = merged_interval
        else:
            result.append(interval1)
            interval1 = intervals[i+1]

    result.append(interval1)
    return result


def _merge_interval(interval1: tuple[int, int], interval2: tuple[int, int]) -> Optional[tuple[int, int]]:
    x1 = max(interval1[0], interval2[0])
    x2 = min(interval1[1], interval2[1])
    if x2 - x1 < 0:
        return None
    return min(interval1[0], interval2[0]), max(interval1[1], interval2[1])

