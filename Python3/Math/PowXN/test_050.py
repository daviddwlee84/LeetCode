from Naive050 import Solution as naive
from Recursive050 import Solution as recursive
from Recursive2_050 import Solution as recursive2
from BitManipulation050 import Solution as bitmanipulation

testcase = [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25000),
    # (0.00001, 2147483647, 0.00000)  # this will TLE on naive solution
]


def test_naive():
    for x, n, ans in testcase:
        assert round(naive().myPow(x, n), 5) == ans


def test_recursive():
    for x, n, ans in testcase:
        assert round(recursive().myPow(x, n), 5) == ans


def test_recursive2():
    for x, n, ans in testcase:
        assert round(recursive2().myPow(x, n), 5) == ans


def test_bitmanipulation():
    for x, n, ans in testcase:
        assert round(bitmanipulation().myPow(x, n), 5) == ans
