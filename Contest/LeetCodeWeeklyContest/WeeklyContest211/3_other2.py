from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        Alex Wice's Solution
        Bottom-up DP

        dp[i][j] = best score for team of people[i:], where everyone has score >= people[j][1]
        """
        n = len(scores)
        people = sorted(zip(ages, scores))

        dp = [[0] * n for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            s = people[i][1]
            for j in range(n):
                dp[i][j] = dp[i + 1][j]
                team_score = people[j][1]
                if s >= team_score:
                    dp[i][j] = max(dp[i][j], s + dp[i + 1][i])

        return max(dp[0])

# Runtime: 7092 ms, faster than 33.33% of Python3 online submissions for Best Team With No Conflicts.
# Memory Usage: 25.1 MB, less than 33.33% of Python3 online submissions for Best Team With No Conflicts.
