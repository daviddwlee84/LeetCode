from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[j] == num:
                    count += 1

        return count
