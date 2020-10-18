from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        https://leetcode.com/problems/minimum-cost-to-cut-a-stick/discuss/877541/Python3-Top-down-DP-Solution-with-comments-and-brief-explanations
        """

        @lru_cache(None)
        def dp(start: int, end: int):
            if end - start <= 1:
                return 0

            min_cost = float('inf')
            for c in cuts:
                if start < c < end:
                    min_cost = min(min_cost, end - start +
                                   dp(start, c) + dp(c, end))

            return min_cost if min_cost != float('inf') else 0

        return dp(0, n)

# Runtime: 1576 ms, faster than 44.42% of Python3 online submissions for Minimum Cost to Cut a Stick.
# Memory Usage: 17.5 MB, less than 5.26% of Python3 online submissions for Minimum Cost to Cut a Stick.
