import pytest

from d5p1 import check_valid, process_rule


@pytest.mark.parametrize("update,expected", [
    ([75,47,61,53,29], True),
    ([97,61,53,29,13], True),
    ([75,29,13], True),
    ([75,97,47,61,53], False),
    ([61,13,29], False),
    ([97,13,75,29,47], False),
])
def test_check_levels(update, expected):
    lines = [
        '47 | 53',
        '97 | 13',
        '97 | 61',
        '97 | 47',
        '75 | 29',
        '61 | 13',
        '75 | 53',
        '29 | 13',
        '97 | 29',
        '53 | 29',
        '61 | 53',
        '97 | 53',
        '61 | 29',
        '47 | 13',
        '75 | 47',
        '97 | 75',
        '47 | 61',
        '75 | 61',
        '47 | 29',
        '75 | 13',
        '53 | 13',
    ]
    rules = {}
    for line in lines:
        rules = process_rule(rules, line)

    assert check_valid(update, rules) == expected
