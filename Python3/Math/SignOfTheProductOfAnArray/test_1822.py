from Python1822 import Solution as Python
from Naive1822 import Solution as Naive
from Better1822 import Solution as Better

testcases = [
    ([-1, -2, -3, -4, 3, 2, 1], 1),
    ([1, 5, 0, 2 - 3], 0),
    ([-1, 1, -1, 1, -1], -1),
]


def test_Python():
    for nums, ans in testcases:
        assert Python().arraySign(nums) == ans


def test_Naive():
    for nums, ans in testcases:
        assert Naive().arraySign(nums) == ans


def test_Better():
    for nums, ans in testcases:
        assert Better().arraySign(nums) == ans
