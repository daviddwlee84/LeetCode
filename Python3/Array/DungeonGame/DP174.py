from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained

        in-place Version
        https://leetcode.com/problems/dungeon-game/discuss/698961/Python-Simple-in-place-DP-solution-O(1)-space
        """

        m, n = len(dungeon), len(dungeon[0])

        # dp[i][j] = minimum hp we need to reach the princess if we start from point (i, j)
        # dummy row and column to handle border cases easier.
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m-1][n], dp[m][n-1] = 1, 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # look at two cells: dp[i+1][j] and dp[i][j+1]
                # evaluate two possible candidates: dp[i+1][j]-dungeon[i][j] and dp[i][j+1]-dungeon[i][j]
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)

        return dp[0][0]

# Runtime: 72 ms, faster than 82.24% of Python3 online submissions for Dungeon Game.
# Memory Usage: 14.8 MB, less than 65.26% of Python3 online submissions for Dungeon Game.
