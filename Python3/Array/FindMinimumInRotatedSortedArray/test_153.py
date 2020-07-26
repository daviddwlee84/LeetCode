from Naive153 import Solution as naive
from Simpler153 import Solution as simpler

testcase = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([1], 1),
    ([2, 1], 1),
    ([1, 2], 1),
    ([2, 3, 4, 5, 1], 1)
]


def test_naive():
    for nums, ans in testcase:
        assert naive().findMin(nums) == ans


def test_simpler():
    for nums, ans in testcase:
        assert simpler().findMin(nums) == ans
