from Naive441 import Solution as naive
from BinarySearch441 import Solution as binarysearch
from Math441 import Solution as math

testcase = [
    (5, 2),
    (8, 3),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (6, 3)
]


def test_naive():
    for n, ans in testcase:
        assert naive().arrangeCoins(n) == ans


def test_binarysearch():
    for n, ans in testcase:
        assert binarysearch().arrangeCoins(n) == ans


def test_math():
    for n, ans in testcase:
        assert math().arrangeCoins(n) == ans
