from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(len(nums) + 1):
            if n not in nums:
                return n
