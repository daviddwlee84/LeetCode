from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position: int, nums: List[int]) -> bool:
        """ recursive function to check if any position can reach the end """
        if position == len(nums) - 1:
            # already at the end
            return True

        furthestJump = min(position + nums[position], len(nums) - 1)

        for nextPosition in reversed(range(position + 1, furthestJump + 1)):
            if self.canJumpFromPosition(nextPosition, nums):
                return True

        return False
