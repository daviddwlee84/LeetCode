from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/solutions/3230797/python-sort-o-nlogn-o-n-greedy/?orderBy=hot
        """
        left = 0
        mid = len(nums) // 2
        right = mid

        nums.sort()
        double_nums = [num * 2 for num in nums]

        answer = 0

        while left < mid and right < len(nums):
            if double_nums[left] <= nums[right]:
                answer += 2
                left += 1
            right += 1

        return answer
