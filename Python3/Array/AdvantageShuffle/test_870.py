from Sorting870 import Solution as Sorting
from SortingWithQueue870 import Solution as SortingWithQueue

testcases = [
    ([2, 7, 11, 15], [1, 10, 4, 11], 4),
    ([12, 24, 8, 32], [13, 25, 32, 11], 3),
]


def test_SortingWithQueue():
    for nums1, nums2, ans in testcases:
        assert sum(num1 > num2 for num1, num2 in zip(
            SortingWithQueue().advantageCount(nums1.copy(), nums2.copy()), nums2)) == ans


def test_Sorting():
    for nums1, nums2, ans in testcases:
        assert sum(num1 > num2 for num1, num2 in zip(
            Sorting().advantageCount(nums1, nums2), nums2)) == ans
