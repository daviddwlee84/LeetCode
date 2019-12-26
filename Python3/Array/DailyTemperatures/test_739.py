from Naive739 import Solution as naive
from Stack739 import Solution as stack

testcase = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([73], [0]),
    ([73, 72], [0, 0]),
    ([72, 73], [1, 0])
]


def test_naive():
    for T, ans in testcase:
        assert naive().dailyTemperatures(T.copy()) == ans


def test_stack():
    for T, ans in testcase:
        assert stack().dailyTemperatures(T) == ans
