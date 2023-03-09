from typing import List
from collections import defaultdict
from functools import lru_cache


# This will TLE
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)

        answer = [0] * n

        @lru_cache()  # TypeError: Expected maxsize to be an integer or None
        def dfs(start: int, curr: int, end: int, distance: int):
            visited.add(curr)

            if curr == end:
                answer[start] += distance
                return

            for neighbor in tree[curr]:
                if neighbor not in visited:
                    dfs(start, neighbor, end, distance + 1)

        for i in range(n):
            for j in range(n):
                visited = set()
                dfs(i, i, j, 0)

        return answer
