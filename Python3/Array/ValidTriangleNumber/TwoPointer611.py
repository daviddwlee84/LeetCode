from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/valid-triangle-number/solutions/1339340/c-java-python-two-pointers-picture-explain-clean-concise-o-n-2/
        """
        nums.sort()

        answer = 0

        # fixed the largest edge
        for right in range(2, len(nums)):
            left = 0
            mid = right - 1

            while left < mid:
                if nums[left] + nums[mid] > nums[right]:
                    # valid triangles
                    # There are `mid-left` valid pairs, because in that case,
                    # when `nums[left]` and `nums[mid]` are fixed,
                    # moving `left` to the right side always causes `nums[left]` + `nums[mid] > nums[right]`
                    answer += mid - left
                    mid -= 1
                else:
                    left += 1

        return answer

# Super complex one: https://leetcode.com/problems/valid-triangle-number/submissions/906858261/
# class Solution(object):
#     def triangleNumber(self, nums):
#         nums.sort()
#         nums = nums[::-1]
#
#         sol = 0
#
#         for i in range(len(nums) - 2):
#             k = len(nums) - 1
#             for j in range(i + 1, k):
#                 if j >= k:
#                     break
#                 diff = nums[i] - nums[j]
#                 while nums[k] <= diff and k > j:
#                     k -= 1
#                 sol += (k - j)
#         return sol
