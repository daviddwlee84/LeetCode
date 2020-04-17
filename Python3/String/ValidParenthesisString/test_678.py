from Naive678 import Solution as naive
from DP678 import Solution as dp
from Greedy678 import Solution as greedy

testcase = [
    ("()", True),
    ("(*)", True),
    ("(*))", True),
    ("())", False),
    ("((*))", True),
    ("(*()", True)
]


def test_naive():
    for s, ans in testcase:
        assert naive().checkValidString(s) == ans


def test_dp():
    for s, ans in testcase:
        assert dp().checkValidString(s) == ans


def test_greedy():
    for s, ans in testcase:
        assert greedy().checkValidString(s) == ans
