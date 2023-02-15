from Naive989 import Solution as Naive
from Python989 import Solution as Python

testcases = [
    ({'num': [1, 2, 0, 0], 'k': 34}, [1, 2, 3, 4]),
    ({'num': [2, 7, 4], 'k': 181}, [4, 5, 5]),
    ({'num': [2, 1, 5], 'k': 806}, [1, 0, 2, 1]),
]


def test_Naive():
    for testcase, ans in testcases:
        assert Naive().addToArrayForm(**testcase) == ans


def test_Python():
    for testcase, ans in testcases:
        assert Python().addToArrayForm(**testcase) == ans
