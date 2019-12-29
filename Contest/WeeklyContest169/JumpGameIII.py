from typing import List
from collections import defaultdict

# [Depth-First Search and Breadth-First Search in Python · Edd Mann](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)
# [Depth First Search or DFS for a Graph - GeeksforGeeks](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        jumpDict = defaultdict(set)
        for i, val in enumerate(arr):
            if 0 <= i + val < len(arr):
                jumpDict[i].add(i + val)
            if 0 <= i - val < len(arr):
                jumpDict[i].add(i - val)

        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if arr[vertex] == 0:
                return True
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(jumpDict[vertex] - visited)

        return False
