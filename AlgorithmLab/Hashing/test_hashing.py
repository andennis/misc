import pytest
from hashing import find_max_length


@pytest.mark.parametrize("nums, result", [
    ([0, 1, 1], 2),
    ([0, 1, 0], 2),
    ([0, 1], 2),
    ([0, 1, 0, 1], 4),
    ([0, 0, 1, 0, 0, 0, 1, 1], 6)
])
def test_find_max_length(nums, result):
    assert find_max_length(nums) == result
