from Naive342 import Solution as Naive
from BitManipulation342 import Solution as BitManipulation
from Iterative342 import Solution as Iterative
from Recursive342 import Solution as Recursive
from Math342 import Solution as Math

testcases = [
    (16, True),
    (5, False),
    (1, True),
    (0, False),
    (-2147483648, False),
]


def test_Naive():
    for n, ans in testcases:
        assert Naive().isPowerOfFour(n) == ans


def test_BitManipulation():
    for n, ans in testcases:
        assert BitManipulation().isPowerOfFour(n) == ans


def test_Iterative():
    for n, ans in testcases:
        assert Iterative().isPowerOfFour(n) == ans


def test_Recursive():
    for n, ans in testcases:
        assert Recursive().isPowerOfFour(n) == ans


def test_Math():
    for n, ans in testcases:
        assert Math().isPowerOfFour(n) == ans
