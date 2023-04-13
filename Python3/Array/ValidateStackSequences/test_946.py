from Naive946 import Solution as Naive
from Better946 import Solution as Better

testcases = [
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ([0, 2, 1], [0, 1, 2], True),
]


def test_Naive():
    for pushed, popped, ans in testcases:
        assert Naive().validateStackSequences(pushed, popped) == ans


def test_Better():
    for pushed, popped, ans in testcases:
        assert Better().validateStackSequences(pushed, popped) == ans
