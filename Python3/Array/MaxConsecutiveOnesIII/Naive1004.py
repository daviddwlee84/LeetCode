from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_left = k
        start, end = 0, -1
        longest_length = 0
        while end < len(nums) - 1:
            if zero_left > 0:
                if nums[end + 1] == 0:
                    zero_left -= 1
                end += 1
            else:
                if nums[end + 1] == 1:
                    end += 1
                else:
                    if nums[start] == 0:
                        # Release a zero
                        zero_left += 1
                    start += 1

            # print(start, end)

            longest_length = max(longest_length, end - start + 1)

        return longest_length

# Runtime: 708 ms, faster than 17.78% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 14.9 MB, less than 32.74% of Python3 online submissions for Max Consecutive Ones III.

# Better solution
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         start = 0
#         # always move right to expand sliding window, move left when k < 0
#         for end in range(len(nums)):
#             if nums[end] == 0:
#                 k -= 1
#             if k < 0:
#                 if nums[start] == 0:
#                     k += 1
#                 start += 1
#         return end - start + 1


# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#
#         start = 0
#         for end in range(len(nums)):
#             k = k - (1 - nums[end])
#
#             if(k < 0):
#                 k = k + (1 - nums[start])
#                 start = start + 1
#         return end - start + 1
