from Naive322 import Solution as naive
from DP322 import Solution as dp

testcase = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([186, 419, 83, 408], 6249, 20),
    ([438, 86, 218, 138, 358, 152, 129], 7656, 19),
    ([413, 213, 453, 20, 150, 321, 254, 396, 487, 234], 5629, 13),
    ([77, 82, 84, 80, 398, 286, 40, 136, 162], 9794, 26),
]


def test_naive():
    for coins, amount, ans in testcase:
        assert naive().coinChange(coins, amount) == ans


def test_dp():
    for coins, amount, ans in testcase:
        assert dp().coinChange(coins, amount) == ans
