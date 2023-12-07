import pytest

from arrays import longest_ones, numSubarrayProductLessThanK


@pytest.mark.parametrize("nums, k, count", [
    # ([0, 0, 0, 0], 0, 0),
    # ([1, 1, 1, 0, 0, 1], 1, 4),
    ([[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0], 1, 6])
])
def test_longest_ones(nums, k, count):
    assert longest_ones(nums, k) == count


@pytest.mark.parametrize("nums, k, count", [
    ([1, 2, 3], 100, 6),
    # ([[10, 5, 2, 6], 100, 8])
])
def test_numSubarrayProductLessThanK(nums, k, count):
    assert numSubarrayProductLessThanK(nums, k) == count
