from typing import List
from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        queue = deque()
        queue.appendleft(source)

        edge_dict = defaultdict(set)
        for u, v in edges:
            edge_dict[u].add(v)
            edge_dict[v].add(u)

        visited = set()
        while queue:
            node = queue.pop()
            visited.add(node)

            for neighbor in edge_dict[node]:
                if neighbor == destination:
                    return True

                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False
