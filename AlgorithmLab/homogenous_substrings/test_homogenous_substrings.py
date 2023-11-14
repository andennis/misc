import pytest
from homogenous_substrings import count_homogenous, MOD_VAL


@pytest.mark.parametrize("st, num", [
    ("", 0),
    ("a", 1),
    ("xy", 2),
    ("aa", 3),
    ("zzzzz", 15),
    ("abbcccaa", 13),
])
def test_count_homogenous(st, num):
    assert count_homogenous(st) % MOD_VAL == num
