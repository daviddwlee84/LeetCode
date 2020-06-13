from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686774/SUGGESTION-FOR-BEGINNERS-SIMPLE-STEPS-BFS-or-DIJKSHTRA-or-DP-DIAGRAM
        """

        # dp[v, k] = Shortest path from src to v using atmost k edges
        dp = [[float('inf') for _ in range(n)] for _ in range(K + 2)]

        for i in range(K + 2):
            # Dist to reach src always zero
            dp[i][src] = 0
        
        for i in range(1, K + 2):
            for start, end, price in flights:
                if dp[i - 1][start] != float('inf'):
                    dp[i][end] = min(dp[i][end], dp[i-1][start] + price)
        
        return dp[K+1][dst] if dp[K+1][dst] != float('inf') else -1

# Runtime: 240 ms, faster than 20.29% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 14.6 MB, less than 84.85% of Python3 online submissions for Cheapest Flights Within K Stops.
