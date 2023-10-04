import pytest

from geom_intersect import intersect_rects, intersect_lines


@pytest.mark.parametrize("rt1,rt2,expected", [
    ((1, 8, 5, 4), (3, 6, 8, 2), (3, 6, 5, 4)),
    ((1, 8, 8, 1), (2, 6, 6, 2), (2, 6, 6, 2)),
    ((2, 6, 6, 2), (2, 6, 6, 2), (2, 6, 6, 2)),
    ((1, 8, 4, 4), (4, 4, 8, 1), (4, 4, 4, 4)),
    ((1, 8, 4, 4), (5, 3, 8, 1), ())
])
def test_intersect_rects(rt1, rt2, expected):
    assert intersect_rects(rt1, rt2) == expected
    assert intersect_rects(rt2, rt1) == expected


@pytest.mark.parametrize("ln1,ln2,expected", [
    ((1, 5), (3, 8), (3, 5)),
    ((1, 8), (2, 5), (2, 5)),
    ((2, 5), (2, 5), (2, 5)),
    ((1, 5), (5, 8), (5, 5)),
    ((1, 4), (6, 8), ())
])
def test_intersect_lines(ln1, ln2, expected):
    assert intersect_lines(ln1, ln2) == expected
    assert intersect_lines(ln2, ln1) == expected
