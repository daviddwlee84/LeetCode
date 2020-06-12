from Naive368 import Solution as naive
from DP368 import Solution as dp

testcase = [
    ([1, 2, 3], [[1, 2], [1, 3]]),
    ([1, 2, 4, 8], [[1, 2, 4, 8]]),
    ([2, 3, 4, 8], [[2, 4, 8]]),
    ([4, 8, 10, 240], [[4, 8, 240]]),
    ([1], [[1]])
]


def test_naive():
    for nums, answers in testcase:
        predict = naive().largestDivisibleSubset(nums)
        assert any([predict == ans for ans in answers]), '%s %s' % (nums, predict)


def test_dp():
    for nums, answers in testcase:
        predict = dp().largestDivisibleSubset(nums)
        assert any([predict == ans for ans in answers]), '%s %s' % (nums, predict)
