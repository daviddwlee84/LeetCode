from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        https://leetcode.com/problems/reconstruct-itinerary/discuss/709877/Python3-DFS-Solution
        https://leetcode.com/problems/reconstruct-itinerary/discuss/710861/Python-Simple-Greedy-DFS-explained-(BEATS-97)
        """
        tickets = sorted(tickets, key=lambda x: x[1], reverse=True)
        edges = defaultdict(list)
        for start, to in tickets:
            edges[start].append(to)

        route = []

        def dfs(airport: str):
            while edges[airport]:
                dfs(edges[airport].pop())
            route.append(airport)

        dfs("JFK")

        return route[::-1]

# Runtime: 80 ms, faster than 81.65% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 14.1 MB, less than 67.37% of Python3 online submissions for Reconstruct Itinerary.
