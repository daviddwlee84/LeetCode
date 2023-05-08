from Naive1572 import Solution as Naive
from Better1572 import Solution as Better

testcases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8),
    ([[5]], 5),
]


def test_Naive():
    for mat, ans in testcases:
        assert Naive().diagonalSum(mat) == ans


def test_Better():
    for mat, ans in testcases:
        assert Better().diagonalSum(mat) == ans
