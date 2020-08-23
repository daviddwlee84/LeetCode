from Naive1475 import Solution as naive
from Stack1475 import Solution as stack

testcase = [
    ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 1, 1, 6], [9, 0, 1, 6]),
    ([10, 1, 1, 6], [9, 0, 1, 6]),
    ([8, 7, 4, 2, 8, 1, 7, 7, 10, 1], [1, 3, 2, 1, 7, 0, 0, 6, 9, 1]),
]


def test_naive():
    for prices, ans in testcase:
        assert naive().finalPrices(prices.copy()) == ans


def test_stack():
    for prices, ans in testcase:
        assert stack().finalPrices(prices.copy()) == ans
