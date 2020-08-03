from Naive520 import Solution as naive
from CapitalCount520 import Solution as capital_count
from RegEx520 import Solution as regex

testcase = [
    ('USA', True),
    ('FlaG', False),
    ('Aaaa', True),
    ('AAaa', False),
    ('aAaa', False),
    ('aaaa', True),
    ('a', True),
    ('A', True),
]


def test_naive():
    for word, ans in testcase:
        assert naive().detectCapitalUse(word) == ans


def test_capital_count():
    for word, ans in testcase:
        assert capital_count().detectCapitalUse(word) == ans


def test_regex():
    for word, ans in testcase:
        assert regex().detectCapitalUse(word) == ans
