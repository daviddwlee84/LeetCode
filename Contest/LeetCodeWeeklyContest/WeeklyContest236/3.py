from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:

        dp = [[float('inf')] * 3 for _ in range(len(obstacles))]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = 1

        for pos in range(1, len(obstacles)):
            # Fill next row first
            # (i.e. go straight first)
            for i in range(3):
                if obstacles[pos] != i + 1:
                    dp[pos][i] = dp[pos][i - 1]

            # Fill next row with rule
            if obstacles[pos] != 1:
                dp[pos][0] = min(dp[pos - 1][0], dp[pos]
                                 [1] + 1, dp[pos][2] + 1)
            if obstacles[pos] != 2:
                dp[pos][1] = min(dp[pos - 1][1], dp[pos]
                                 [0] + 1, dp[pos][2] + 1)
            if obstacles[pos] != 3:
                dp[pos][2] = min(dp[pos - 1][2], dp[pos]
                                 [0] + 1, dp[pos][1] + 1)

            # Run twice...
            if obstacles[pos] != 1:
                dp[pos][0] = min(dp[pos - 1][0], dp[pos]
                                 [1] + 1, dp[pos][2] + 1)
            if obstacles[pos] != 2:
                dp[pos][1] = min(dp[pos - 1][1], dp[pos]
                                 [0] + 1, dp[pos][2] + 1)
            if obstacles[pos] != 3:
                dp[pos][2] = min(dp[pos - 1][2], dp[pos]
                                 [0] + 1, dp[pos][1] + 1)

        return min(dp[len(obstacles) - 1])
