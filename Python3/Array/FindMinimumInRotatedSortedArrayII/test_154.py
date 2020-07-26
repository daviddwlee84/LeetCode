from Naive154 import Solution as naive
from YetAnother154 import Solution as yet_another

testcase = [
    ([1, 3, 5], 1),
    ([2, 2, 2, 0, 1], 0),
    # copied from problem 153
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


def test_yet_another():
    for nums, ans in testcase:
        assert yet_another().findMin(nums) == ans
