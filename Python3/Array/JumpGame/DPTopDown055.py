from typing import List
from enum import Enum


class Index(Enum):
    GOOD = 0
    BAD = 1
    UNKNOWN = 2


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        can be thought of as optimized backtracking
        i.e. memorization

        Time Complexity: O(n^2)
        Space Complexity: O(2n)
        """
        self.memo = [Index.UNKNOWN] * len(nums)
        self.memo[-1] = Index.GOOD
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position: int, nums: List[int]) -> bool:
        if self.memo[position] != Index.UNKNOWN:
            return True if self.memo[position] == Index.GOOD else False

        furthestJump = min(position + nums[position], len(nums) - 1)

        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                self.memo[position] = Index.GOOD
                return True

        self.memo[position] = Index.BAD
        return False
