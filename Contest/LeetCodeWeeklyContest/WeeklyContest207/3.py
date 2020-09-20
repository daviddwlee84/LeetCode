from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        MOD = (10**9 + 7)

        dp = [[[1, -1] for _ in range(len(grid[0]))]
              for _ in range(len(grid))]  # [[(neg max, pos max), ...], ...]
        if grid[0][0] > 0:
            dp[0][0][1] = grid[0][0]
        elif grid[0][0] < 0:
            dp[0][0][0] = grid[0][0]
        else:
            return 0

        for i in range(1, len(grid)):
            if grid[i][0] > 0:
                dp[i][0][0] = grid[i][0] * dp[i - 1][0][0]
                dp[i][0][1] = grid[i][0] * dp[i - 1][0][1]
            elif grid[i][0] < 0:
                dp[i][0][0] = grid[i][0] * dp[i - 1][0][1]
                dp[i][0][1] = grid[i][0] * dp[i - 1][0][0]
            else:
                dp[i][0] = [0, 0]

        for j in range(1, len(grid[0])):
            if grid[0][j] > 0:
                dp[0][j][0] = grid[0][j] * dp[0][j - 1][0]
                dp[0][j][1] = grid[0][j] * dp[0][j - 1][1]
            elif grid[0][j] < 0:
                dp[0][j][0] = grid[0][j] * dp[0][j - 1][1]
                dp[0][j][1] = grid[0][j] * dp[0][j - 1][0]
            else:
                dp[0][j] = [0, 0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] > 0:
                    dp[i][j][0] = min(dp[i - 1][j][0] * grid[i]
                                      [j], dp[i][j - 1][0] * grid[i][j])
                    dp[i][j][1] = max(dp[i - 1][j][1] * grid[i]
                                      [j], dp[i][j - 1][1] * grid[i][j])
                elif grid[i][j] < 0:
                    dp[i][j][0] = min(dp[i - 1][j][1] * grid[i]
                                      [j], dp[i][j - 1][1] * grid[i][j])
                    dp[i][j][1] = max(dp[i - 1][j][0] * grid[i]
                                      [j], dp[i][j - 1][0] * grid[i][j])
                else:
                    dp[i][j] = [0, 0]

        if dp[-1][-1][1] < 0:
            return -1

        return dp[-1][-1][1] % MOD

# [[2, 1, 3, 0, -3, 3, -4, 4, 0, -4],
# [-4, -3, 2, 2, 3, -3, 1, -1, 1, -2],
# [-2, 0, -4, 2, 4, -3, -4, -1, 3, 4],
# [-1 ,0 ,1, 0, -3 ,3, -2, -3, 1, 0],
# [0,-1 ,- 2,0 ,- 3, -4, 0,3 ,-2 ,- 2],
# [-4, -2 ,0, -1 ,0 ,-3 ,0, 4,0 ,- 3],
# [-3,- 4, 2,1 ,0 ,- 4,2 ,-4 ,-1 ,- 3],
# [3,- 2, 0,- 4, 1, 0,1 ,-3 ,-1 ,- 1],
# [3, -4 ,0, 2, 0, -2, 2,- 4,- 2, 4],
# [0,4,0,-3,-4,3,3,-1,-2,-2]]
#
# 19215865
#
# if you forgot to apply MOD....
