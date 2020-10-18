from typing import List
from functools import lru_cache


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        Alex Wice's Solution
        Top-down DP
        """
        n = len(scores)
        people = sorted(zip(ages, scores))

        @lru_cache(None)
        def dp(i: int, team_score: int):
            """
            team_score: maximum team score of team I picked from people[:i]
            """
            if i == n:
                return 0

            s = people[i][1]
            ans = dp(i + 1, team_score)
            if s >= team_score:
                ans = max(ans, s + dp(i + 1, s))

            return ans

        return dp(0, 0)

# Memory Limit Exceeded
# https://leetcode.com/submissions/detail/410103987/testcase/
