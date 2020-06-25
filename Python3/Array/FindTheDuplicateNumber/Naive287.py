
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num in nums[i+1:]:
                return num

# Runtime: 6228 ms, faster than 5.01% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.3 MB, less than 55.80% of Python3 online submissions for Find the Duplicate Number.
