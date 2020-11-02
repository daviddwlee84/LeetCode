from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memo = set()
        for num in nums:
            if num in memo:
                return num
            memo.add(num)

# Runtime: 64 ms, faster than 73.62% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 18.1 MB, less than 17.96% of Python3 online submissions for Find the Duplicate Number.
