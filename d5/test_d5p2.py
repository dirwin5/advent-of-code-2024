import pytest

from d5p2 import check_valid, process_rule, fix_order

LINES = [
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


@pytest.mark.parametrize("update,expected", [
    ([75, 47, 61, 53, 29], [75, 47, 61, 53, 29]),
    ([97, 61, 53, 29, 13], [97, 61, 53, 29, 13]),
    ([75, 29, 13], [75, 29, 13]),
    ([75, 97, 47, 61, 53], [97, 75, 47, 61, 53]),
    ([61, 13, 29], [61, 29, 13]),
    ([97, 13, 75, 29, 47], [97, 75, 47, 29, 13]),
])
def test_fix_order(update, expected):
    rules = {}
    for line in LINES:
        rules = process_rule(rules, line)

    assert fix_order(update, rules) == expected


@pytest.mark.parametrize("update,expected", [
    ([75, 47, 61, 53, 29], True),
    ([97, 61, 53, 29, 13], True),
    ([75, 29, 13], True),
    ([75, 97, 47, 61, 53], False),
    ([61, 13, 29], False),
    ([97, 13, 75, 29, 47], False),
])
def test_check_levels(update, expected):
    rules = {}
    for line in LINES:
        rules = process_rule(rules, line)

    assert check_valid(update, rules) == expected
