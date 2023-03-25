from typing import List
from collections import deque, defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        queue = deque([0])

        correct_path = set()
        while queue:
            node = queue.pop()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    correct_path.add((neighbor, node))
                    queue.appendleft(neighbor)

        # print(correct_path)
        answer = 0
        for u, v in connections:
            if (u, v) not in correct_path:
                answer += 1

        return answer
