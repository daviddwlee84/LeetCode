from BruteForce300 import Solution as bruteForce
from MemoryRecursive300 import Solution as memoryRecursive
from DP300 import Solution as DP
from BinarySearch300 import Solution as BS

testcase = [
    ([10,9,2,5,3,7,101,18], 4),
    ([1,3,6,7,9,4,10,5,6], 6)
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

def test_BF():
    for nums, ans in testcase:
        assert BS().lengthOfLIS(nums) == ans
