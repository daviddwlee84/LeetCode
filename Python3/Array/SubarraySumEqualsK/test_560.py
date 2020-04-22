from BruteForce560 import Solution as bruteForce
from CumulativeSum560 import Solution as cumulativeSum
from WithoutSpace560 import Solution as withoutSpace
from HT560 import Solution as hashTable

testcase = [
    ([1, 1, 1], 2, 2),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4)
]

def test_bruteForce():
    for nums, k, ans in testcase:
        assert bruteForce().subarraySum(nums, k) == ans

def test_cumulativeSum():
    for nums, k, ans in testcase:
        assert cumulativeSum().subarraySum(nums, k) == ans

def test_withoutSpace():
    for nums, k, ans in testcase:
        assert withoutSpace().subarraySum(nums, k) == ans

def test_hashTable():
    for nums, k, ans in testcase:
        assert hashTable().subarraySum(nums, k) == ans
