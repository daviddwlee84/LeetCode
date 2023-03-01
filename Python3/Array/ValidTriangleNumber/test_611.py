from BruteForce611 import Solution as BruteForce
from BinarySearch611 import Solution as BinarySearch
from BinarySearch2_611 import Solution as BinarySearch2
from TwoPointer611 import Solution as TwoPointer

testcases = [
    ([2, 2, 3, 4], 3),
    ([4, 2, 3, 4], 4),
]

def test_BruteForce():
    for nums, ans in testcases:
        assert BruteForce().triangleNumber(nums) == ans


def test_BinarySearch():
    for nums, ans in testcases:
        assert BinarySearch().triangleNumber(nums) == ans


def test_BinarySearch2():
    for nums, ans in testcases:
        assert BinarySearch2().triangleNumber(nums) == ans


def test_TwoPointer():
    for nums, ans in testcases:
        assert TwoPointer().triangleNumber(nums) == ans


