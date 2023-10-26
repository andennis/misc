import pytest
from servers_map import servers_interacted_count

TEST_SRV_MAP = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
]


@pytest.mark.parametrize("srvs_map, count", [
    ([], 0),
    ([[0]], 0),
    ([[0, 0]], 0),
    ([[1]], 0),
    ([[1, 0]], 0),
    ([[1, 0, 1]], 2),
    ([[0], [0]], 0),
    ([[0], [1]], 0),
    ([[1], [1]], 2),
    (TEST_SRV_MAP, 6),
])
def test_servers_interacted_count(srvs_map, count):
    assert servers_interacted_count(srvs_map) == count
