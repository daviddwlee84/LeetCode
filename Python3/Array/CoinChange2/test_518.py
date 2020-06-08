from Naive518 import Solution as naive
from DP518 import Solution as DP

testcase = [
    (5, [1, 2, 5], 4),
    (3, [2], 0),
    (10, [10], 1),
    (0, [], 1),
    # (500, [3, 5, 7, 8, 9, 10, 11], 87)
]


def test_naive():
    for amount, coins, ans in testcase:
        assert naive().change(amount, coins) == ans


def test_DP():
    for amount, coins, ans in testcase:
        assert DP().change(amount, coins) == ans
