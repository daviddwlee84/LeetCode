# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (36.95%)
# Likes:    1417
# Dislikes: 3250
# Total Accepted:    447.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # key is to handle numbers from the largest number
        while m > 0 and n > 0:
            # put the largest number to the end
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # if the n > 0 i.e. still element left in nums2
        # or special case that nums1 is empty
        if n > 0:
            # just copy the rest of nums2 to nums1
            nums1[:n] = nums2[:n]

# 59/59 cases passed (28 ms)
# Your runtime beats 99.53 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
