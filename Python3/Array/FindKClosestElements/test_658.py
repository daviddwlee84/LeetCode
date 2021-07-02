from Naive658 import Solution as naive
from DoubleSort658 import Solution as doublesort
from FindLeftBound658 import Solution as leftbound

testcases = [
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, 100, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 3, 3, [2, 3, 4]),
    ([1, 2, 3, 4, 5], 3, -1, [1, 2, 3]),
    ([1, 1, 1, 10, 10, 10], 1, 9, [10]),
    ([1], 1, 0, [1]),
    ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4])
]


def test_naive():
    for arr, k, x, ans in testcases:
        assert list(naive().findClosestElements(arr, k, x)) == ans


def test_doublesort():
    for arr, k, x, ans in testcases:
        assert list(doublesort().findClosestElements(arr, k, x)) == ans


def test_leftbound():
    for arr, k, x, ans in testcases:
        assert list(leftbound().findClosestElements(arr, k, x)) == ans
