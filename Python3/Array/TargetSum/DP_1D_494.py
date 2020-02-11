from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [0] * 2001
        dp[nums[0] + 1000] += 1
        dp[-nums[0] + 1000] += 1

        for i in range(1, len(nums)):
            # create a temp dp for the next position
            next_dp = [0] * 2001
            for s in range(-1000, 1001):
                if dp[s + 1000] > 0:
                    next_dp[s + nums[i] + 1000] += dp[s + 1000]
                    next_dp[s - nums[i] + 1000] += dp[s + 1000]
            # update dp
            dp = next_dp

        return 0 if S > 1000 else dp[S + 1000]

# Runtime: 484 ms, faster than 22.72% of Python3 online submissions for Target Sum.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Target Sum.
