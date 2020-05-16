from Naive918 import Solution as naive
from MinSumSubarray918 import Solution as minSumSubarray

testcase = [
    ([1, -2, 3, -2], 3),
    ([5, -3, 5], 10),
    ([3, -1, 2, -1], 4),
    ([3, -2, 2, -3], 3),
    ([-2, -3, -1], -1)
]


def test_naive():
    for A, ans in testcase:
        assert naive().maxSubarraySumCircular(A) == ans


def test_minSumSubarray():
    for A, ans in testcase:
        assert minSumSubarray().maxSubarraySumCircular(A) == ans
