from BinarySearch875 import Solution as bs
from Naive875 import Solution as naive

testcase = [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),
    # ([312884470], 312884469, 2)
]


def test_naive():
    for piles, H, ans in testcase:
        assert naive().minEatingSpeed(piles, H) == ans


def test_bs():
    for piles, H, ans in testcase:
        assert bs().minEatingSpeed(piles, H) == ans
