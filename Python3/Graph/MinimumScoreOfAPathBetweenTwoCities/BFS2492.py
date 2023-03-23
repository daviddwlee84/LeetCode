from typing import List
from collections import deque, defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solutions/3326775/image-explanation-both-bfs-dfs-approaches-c-java-python-union-find-is-overrated/
        """
        edges = defaultdict(list)
        for u, v, distance in roads:
            edges[u].append((v, distance))
            edges[v].append((u, distance))

        queue = deque([1])
        visited = set([1])
        answer = float('inf')
        while queue:
            node = queue.pop()
            for neighbor, distance in edges[node]:
                # This will alway update the answer even not visit
                answer = min(answer, distance)
                if neighbor not in visited:
                    queue.appendleft(neighbor)
                    visited.add(neighbor)
        return answer
