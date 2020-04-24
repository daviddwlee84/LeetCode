from typing import List
from enum import Enum


class Index(Enum):
    GOOD = 0
    BAD = 1
    UNKNOWN = 2


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Top-down to bottom-up conversion is done by eliminating recursion

        benefit
        * no method stack overhead
        * might benefit from come caching
        * open up possibilities for future optimization

        eliminating recursion: usually by trying to reverse the order of the steps

        Time Complexity: O(n^2)
        Space Complextiy: O(n)
        """
        memo = [Index.UNKNOWN] * len(nums)
        memo[-1] = Index.GOOD

        # start from the position right before the end
        for i in reversed(range(len(nums) - 1)):

            # if any next position in jump range can reach good, then it is good
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break

        # state of the start is the answer
        return memo[0] == Index.GOOD
