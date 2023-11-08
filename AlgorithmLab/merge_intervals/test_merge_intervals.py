import pytest
from merge_intervals import merge_intervals


@pytest.mark.parametrize("intervals, expected", [
    ([(1, 5), (1, 2), (1, 7)], [(1, 7)]),
    ([(1, 5), (5, 7)], [(1, 7)]),
    ([(5, 7), (1, 5)], [(1, 7)]),
    ([(1, 5), (3, 7)], [(1, 7)]),
    ([(3, 7), (1, 5)], [(1, 7)]),
    ([(1, 3), (5, 7)], [(1, 3), (5, 7)]),
    ([(5, 7), (1, 3)], [(1, 3), (5, 7)]),
    ([(1, 8), (3, 7)], [(1, 8)]),
    ([(3, 7), (1, 8)], [(1, 8)]),
    ([(16, 18), (1, 5), (3, 7), (10, 14), (9, 11), (0, 3), (2, 4)], [(0, 7), (9, 14), (16, 18)]),
])
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected
