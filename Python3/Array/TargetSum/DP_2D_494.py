from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # Store the summation at each position
        # len(nums) * 2001
        # 2001 is because "The sum of elements in the given array will not exceed 1000"
        # So the sum range will be between -1000~1000 (include number 0) => 2001
        # The 1000 is the offset to map index 0~2001 to -1000~1000
        dp = [[0 for _ in range(2001)] for _ in range(len(nums))]

        # base case (+ or - the first number)
        # use += is because when nums[0] is 0, there will access the same dp slot
        dp[0][nums[0] + 1000] += 1
        dp[0][-nums[0] + 1000] += 1

        # loop for each position & sum
        for i in range(1, len(nums)):
            # for each position check each sum
            for s in range(-1000, 1001):
                # if there is some value in the last position
                if dp[i - 1][s + 1000] > 0:
                    dp[i][s + nums[i] + 1000] += dp[i - 1][s + 1000]
                    dp[i][s - nums[i] + 1000] += dp[i - 1][s + 1000]

        # if S > 1000, it doesn't match the limitation of the problem
        # otherwise the last position of S is the answer
        return 0 if S > 1000 else dp[len(nums) - 1][S + 1000]
