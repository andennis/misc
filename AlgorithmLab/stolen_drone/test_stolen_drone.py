import pytest
from stolen_drone import find_stolen_drones


@pytest.mark.parametrize("all_drones, stolen_drones", [
    ([1, 2, 1], [2]),
    ([1, 2, 2, 1], []),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 2, 1], [3, 4])
])
def test_find_stolen_drones(all_drones, stolen_drones):
    assert set(find_stolen_drones(all_drones)) == set(stolen_drones)

