import pytest

from arrays import longest_ones


@pytest.mark.parametrize("nums, k, count", [
    # ([0, 0, 0, 0], 0, 0),
    # ([1, 1, 1, 0, 0, 1], 1, 4),
    ([[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0], 1, 6])
])
def test_longest_ones(nums, k, count):
    assert longest_ones(nums, k) == count
