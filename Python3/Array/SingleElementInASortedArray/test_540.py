from Naive540 import Solution as Naive
from BinarySearchXOR540 import Solution as BinarySearchXOR
from XOR540 import Solution as XOR
from BinarySearch540 import Solution as BinarySearch

testcases = [
    ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
    ([3, 3, 7, 7, 10, 11, 11], 10),
]


def test_Naive():
    for nums, ans in testcases:
        assert Naive().singleNonDuplicate(nums) == ans


def test_BinarySearchXOR():
    for nums, ans in testcases:
        assert BinarySearchXOR().singleNonDuplicate(nums) == ans


def test_XOR():
    for nums, ans in testcases:
        assert XOR().singleNonDuplicate(nums) == ans


def test_BinarySearch():
    for nums, ans in testcases:
        assert BinarySearch().singleNonDuplicate(nums) == ans
