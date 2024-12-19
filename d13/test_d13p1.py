import pytest

from d13p1 import solve_bn


@pytest.mark.parametrize("ax, ay, bx, by, prizex, prizey, expected", [
    (94, 34, 22, 67, 8400, 5400, 40),
    (26, 66, 67, 21, 12748, 12176, -1),
    (17, 86, 84, 37, 7870, 6450, 86),
    (46, 98, 57, 16, 5659, 9842, 21),
    (60, 46, 13, 34, 4801, 4570, 37),
])
def test_solve_bn(ax, ay, bx, by, prizex, prizey, expected):
    low = 0
    high = 100
    assert solve_bn(low, high, ax, ay, bx, by, prizex, prizey) == expected
