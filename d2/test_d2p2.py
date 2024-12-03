import pytest

from d2p2 import check_levels


@pytest.mark.parametrize("levels,expected", [
    ([16, 19, 21, 24, 21], False),
    ([16, 19, 21, 21], False),
    ([16, 19, 21, 24], True),
    ([1, 2, 3, 4, 5], True),
    ([7, 2, 3, 4, 5], False),
    ([3, 2, 3, 4, 5], False),
    ([2, 3, 4, 5], True),
    ([4, 3, 2, 3, 4, 5], False),
])
def test_check_levels(levels, expected):
    assert check_levels(levels) == expected
