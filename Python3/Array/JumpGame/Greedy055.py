from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Track the "left-most GOOD position"
        (observed from the break statement)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        lastPos = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0
