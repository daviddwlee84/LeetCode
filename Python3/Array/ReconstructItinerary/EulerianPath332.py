from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        https://leetcode.com/problems/reconstruct-itinerary/discuss/709590/Python-Short-Euler-Path-Finding-O(E-log-E)-explained.

        http://www.graph-magics.com/articles/euler.php
        https://leetcode.com/problems/reconstruct-itinerary/discuss/709531/Eulerian-Path-in-Directed-Graph-or-Recursive-or-Iterative

        Eulerian Path: Given an undirected or a directed graph, find a path or circuit that passes through each edge exactly once.
        """
        self.route = []
        self.edges = defaultdict(list)
        for start, to in tickets:
            heapq.heappush(self.edges[start], to)

        self.dfs("JFK")
        return list(reversed(self.route))

    def dfs(self, airport: str):
        while self.edges[airport]:
            candidate = heapq.heappop(self.edges[airport])
            self.dfs(candidate)
        self.route.append(airport)

# Runtime: 84 ms, faster than 66.50% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 14.2 MB, less than 47.83% of Python3 online submissions for Reconstruct Itinerary.
