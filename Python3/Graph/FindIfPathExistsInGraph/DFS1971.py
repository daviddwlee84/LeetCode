from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        edge_dict = defaultdict(set)
        for u, v in edges:
            edge_dict[u].add(v)
            edge_dict[v].add(u)

        visited = set()

        def dfs(node: int) -> bool:
            visited.add(node)
            for neighbor in edge_dict[node]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
