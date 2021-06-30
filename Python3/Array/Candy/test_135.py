from BruteForce135 import Solution as BruteForce
from TwoArrays135 import Solution as TwoArrays

testcases = [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([29, 51, 87, 87, 72, 12], 12),
]


def test_BruteForce():
    for ratings, ans in testcases:
        assert BruteForce().candy(ratings) == ans


def test_TwoArrays():
    for ratings, ans in testcases:
        assert TwoArrays().candy(ratings) == ans
