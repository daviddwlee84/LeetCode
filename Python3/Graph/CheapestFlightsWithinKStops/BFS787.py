from typing import List
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686774/SUGGESTION-FOR-BEGINNERS-SIMPLE-STEPS-BFS-or-DIJKSHTRA-or-DP-DIAGRAM
        """

        if src == dst:
            return 0

        costs = defaultdict(lambda: float('inf'))
        
        edges = defaultdict(list)
        for start, end, price in flights:
            edges[start].append((end, price))
        
        queue = deque([(src, -1, 0)]) # start, k, cost

        while queue:
            curr_city, k, cost = queue.pop()
            
            if curr_city == dst or k == K:
                # Early stop
                continue
        
            for end, price in edges[curr_city]:
                if cost + price >= costs[end]:
                    # Early stop
                    continue
                
                costs[end] = cost + price
                queue.appendleft((end, k+1, cost + price))
        
        return costs[dst] if costs[dst] < float('inf') else -1

# Runtime: 72 ms, faster than 99.32% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 14.8 MB, less than 65.79% of Python3 online submissions for Cheapest Flights Within K Stops.