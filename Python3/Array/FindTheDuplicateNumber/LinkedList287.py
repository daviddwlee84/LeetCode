from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] *= -1

# Runtime: 68 ms, faster than 49.62% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.3 MB, less than 17.96% of Python3 online submissions for Find the Duplicate Number.
