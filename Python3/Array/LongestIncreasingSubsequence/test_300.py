from BruteForce300 import Solution as bruteForce
from MemoryRecursive300 import Solution as memoryRecursive
from DP300 import Solution as DP
from DP2_300 import Solution as DP2
from BinarySearch300 import Solution as BS
from BinarySearch2_300 import Solution as BS2

testcase = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
]


def test_bruteForce():
    for nums, ans in testcase:
        assert bruteForce().lengthOfLIS(nums) == ans


def test_memoryRecursive():
    for nums, ans in testcase:
        assert memoryRecursive().lengthOfLIS(nums) == ans


def test_DP():
    for nums, ans in testcase:
        assert DP().lengthOfLIS(nums) == ans


def test_DP2():
    for nums, ans in testcase:
        assert DP2().lengthOfLIS(nums) == ans


def test_BS():
    for nums, ans in testcase:
        assert BS().lengthOfLIS(nums) == ans


def test_BS2():
    for nums, ans in testcase:
        assert BS2().lengthOfLIS(nums) == ans
