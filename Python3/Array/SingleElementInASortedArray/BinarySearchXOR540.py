from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """ https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627786/C%2B%2B-O(log-n)-time-O(1)-space-or-Simple-and-clean-or-Use-xor-to-keep-track-of-odd-even-pair
        nums[mid] == nums[mid ^ 1] for odd position compares with the previous number; for even position compares with the next number.
        The unique number must be at even position.
        """

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            # print(start, end, mid, mid ^ 1)
            if nums[mid] == nums[mid ^ 1]:
                start = mid + 1
            else:
                end = mid
        
        return nums[start]

# Runtime: 76 ms, faster than 46.02% of Python3 online submissions for Single Element in a Sorted Array.
# Memory Usage: 16.1 MB, less than 7.69% of Python3 online submissions for Single Element in a Sorted Array.

# Other Binary Search
# 
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         low = 0
#         high = len(nums) - 1
#         while True:
#             mid = (low + high) // 2
#             if mid % 2 == 1:
#                 mid -= 1
#             if mid < high and nums[mid] == nums[mid+1]:
#                 low = mid + 2
#             elif mid > low and nums[mid] == nums[mid-1]:
#                 high = mid - 2
#             else:
#                 return nums[mid]