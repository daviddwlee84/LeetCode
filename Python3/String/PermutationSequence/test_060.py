from Naive060 import Solution as naive
from Math060 import Solution as math
from Backtracking060 import Solution as backtracking

testcase = [
    (3, 3, '213'),
    (4, 9, '2314'),
    (9, 37098, '194627853')
]


def test_naive():
    for n, k, ans in testcase:
        assert naive().getPermutation(n, k) == ans


def test_backtracking():
    for n, k, ans in testcase:
        assert backtracking().getPermutation(n, k) == ans


def test_math():
    for n, k, ans in testcase:
        assert math().getPermutation(n, k) == ans
