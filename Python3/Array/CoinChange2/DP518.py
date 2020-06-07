from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1

        for j in range(1, len(coins) + 1):
            # Number ways of selecting for amount zero is 1
            dp[j][0] = 1
            for i in range(1, amount + 1):
                # exclude current coin
                dp[j][i] = dp[j - 1][i]

                # check if amount >= to the current ith coin
                if i - coins[j - 1] >= 0:
                    # include current coin
                    dp[j][i] += dp[j][i - coins[j - 1]]

        return dp[len(coins)][amount]

# Runtime: 1032 ms, faster than 11.00% of Python3 online submissions for Coin Change 2.
# Memory Usage: 29.7 MB, less than 21.00% of Python3 online submissions for Coin Change 2.
