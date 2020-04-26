from Naive221 import Solution as naive
from BruteForce221 import Solution as bruteForce
from DP221 import Solution as DP
from DP_2_221 import Solution as betterDP

testcase = [
    ([], 0),
    ([["1"]], 1),
    ([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
     "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]], 4)
]


def test_naive():
    for matrix, ans in testcase:
        assert naive().maximalSquare(matrix) == ans


def test_bruteForce():
    for matrix, ans in testcase:
        assert bruteForce().maximalSquare(matrix) == ans


def test_DP():
    for matrix, ans in testcase:
        assert DP().maximalSquare(matrix) == ans


def test_betterDP():
    for matrix, ans in testcase:
        assert betterDP().maximalSquare(matrix) == ans
