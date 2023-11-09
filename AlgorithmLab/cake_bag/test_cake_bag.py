import pytest
from cake_bag import max_duffel_bag_value


@pytest.mark.parametrize("cakes, capacity, result", [
    ([(0, 5)], 5, 0),
    ([(0, 0), (1, 0), (2, 1)], 5, 2),
    ([(3, 2), (2, 1)], 0, 0),
    ([(7, 160), (3, 90), (2, 15)], 20, 555),
    ([(2, 1), (3, 3)], 5, 4),
    ([(2, 1), (4, 5)], 5, 5),
    ([(10, 1), (1, 1)], 10, 10),
    ([(3, 2), (2, 1)], 11, 7),
])
def test_cake_bag(cakes, capacity, result):
    assert max_duffel_bag_value(cakes, capacity) == result
