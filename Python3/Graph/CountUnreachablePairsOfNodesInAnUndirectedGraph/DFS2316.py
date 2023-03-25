from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/solutions/3337616/simple-dfs-count-number-of-nodes-in-connected-components-c/?orderBy=hot
        """
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        answer = 0

        visited = set()

        # Find each group using DFS
        group_sizes = []

        def dfs(x: int):
            if x in visited:
                return
            visited.add(x)
            group_sizes[-1] += 1
            for neighbor in graph[x]:
                dfs(neighbor)

        for i in range(n):
            if i in visited:
                continue
            group_sizes.append(0)
            dfs(i)
        
        # print(group_sizes)

        answer = 0
        # Math part
        temp = 0
        for group_size in group_sizes:
            answer += group_size * (n - temp - group_size)
            temp += group_size
        return answer
