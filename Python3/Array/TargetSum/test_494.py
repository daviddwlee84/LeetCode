from Naive494 import Solution as naive
from RecursiveWithMemory494 import Solution as recursive_mem
from DP_2D_494 import Solution as DP_2D
from DP_1D_494 import Solution as DP_1D

testcase = [
    ([8, 48, 11, 47, 26, 12, 16, 39, 38, 50, 21,
      12, 34, 1, 28, 1, 3, 9, 17, 50], 3, 6317),
    ([1, 1, 1, 1, 1], 3, 5),
    ([1], 1, 1),
    ([1], 0, 0),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256)
]


def test_naive():
    for nums, S, output in testcase:
        assert naive().findTargetSumWays(nums.copy(), S) == output


def test_recursive_with_memory():
    for nums, S, output in testcase:
        assert recursive_mem().findTargetSumWays(nums.copy(), S) == output


def test_dp2d():
    for nums, S, output in testcase:
        assert DP_2D().findTargetSumWays(nums.copy(), S) == output


def test_dp1d():
    for nums, S, output in testcase:
        assert DP_1D().findTargetSumWays(nums.copy(), S) == output
