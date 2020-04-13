from Naive525 import Solution as naive
from HT525 import Solution as ht

testcase = [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 1, 0, 1], 4)
]


def test_naive():
    for nums, ans in testcase:
        assert naive().findMaxLength(nums) == ans


def test_ht():
    for nums, ans in testcase:
        assert ht().findMaxLength(nums) == ans
