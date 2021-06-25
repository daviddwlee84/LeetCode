from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Time complexity: O(N^2)
        Space complexity: O(N)

        Runtime: 80 ms, faster than 24.02% of Python3 online submissions for Redundant Connection.
        Memory Usage: 15.4 MB, less than 9.85% of Python3 online submissions for Redundant Connection.
        """
        graph = defaultdict(set)

        def dfs(source: int, target: int, seen: set) -> bool:
            """
            To test if we can connect from source to target
            https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
            https://stackoverflow.com/questions/45869507/python-should-i-use-parameters-or-make-it-global
            """
            if source not in seen:
                seen.add(source)

                if source == target:
                    return True
                # else try to travel all its neighbors (we only need to find a single route)
                return any(dfs(neighbor, target, seen) for neighbor in graph[source])

        for u, v in edges:
            # Each time we add a new edge, we check it again
            seen = set()

            if u in graph and v in graph and dfs(u, v, seen):
                return u, v

            graph[u].add(v)
            graph[v].add(u)
