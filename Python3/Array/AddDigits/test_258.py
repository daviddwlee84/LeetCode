from Naive258 import Solution as naive
from NoLoop258 import Solution as no_loop
from Iterative258 import Solution as iterative

testcase = [
    (38, 2),
    (11, 2),
    (2, 2),
    (10, 1)
]


def test_naive():
    for num, ans in testcase:
        assert naive().addDigits(num) == ans


def test_no_loop():
    for num, ans in testcase:
        assert no_loop().addDigits(num) == ans


def test_iterative():
    for num, ans in testcase:
        assert iterative().addDigits(num) == ans
