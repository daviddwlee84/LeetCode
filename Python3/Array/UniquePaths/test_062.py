from Naive062 import Solution as naive
from DP062 import Solution as DP

testcase = [
    (3, 2, 3),
    (7, 3, 28),
    (57, 2, 57),
]


def test_naive():
    for m, n, ans in testcase:
        assert naive().uniquePaths(m, n) == ans


def test_DP():
    for m, n, ans in testcase:
        assert DP().uniquePaths(m, n) == ans
