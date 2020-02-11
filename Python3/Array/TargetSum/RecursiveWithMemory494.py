from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        return self.helper(nums, S, 0, S)

    def helper(self, nums: List[int], S: int, curIdx: int, targetSum: int):
        """
        curIdx: backtracking progress
        targetSum: the number left to reach the S (to be reduced to 0)
        """
        # Trick to locate case in memory
        curSerial = self.getIndex(curIdx, targetSum)
        if curSerial in self.memo:
            # If found in memory, then just return
            return self.memo.get(curSerial)

        if curIdx == len(nums):
            # If reach the end (base case)
            if targetSum == 0:
                return 1
            return 0

        # Calculate the number of ways (if this case haven't happened before and is not the base case)
        numWaysIfAdd = self.helper(
            nums, S, curIdx + 1, targetSum + nums[curIdx])
        numWaysIfMinus = self.helper(
            nums, S, curIdx + 1, targetSum - nums[curIdx])

        numWays = numWaysIfAdd + numWaysIfMinus
        self.memo[curSerial] = numWays
        return numWays

    def getIndex(self, curIdx: int, targetSum: int):
        """ Serialize the current state """
        return "%d,%d" % (curIdx, targetSum)

# Runtime: 636 ms, faster than 15.38% of Python3 online submissions for Target Sum.
# Memory Usage: 13.4 MB, less than 75.00% of Python3 online submissions for Target Sum.
