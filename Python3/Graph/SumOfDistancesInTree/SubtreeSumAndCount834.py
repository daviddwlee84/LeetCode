from typing import List
from collections import defaultdict


class Solution(object):
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Convert edges in to graph representation
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        ans = [0] * n
        # Count children for each subtree when each node as a root
        count = [1] * n

        def dfs(node: int = 0, parent: int = None):
            """
            Post-order traversal
            Store sub-tree sum in ans
            Store child count in count
            """
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node: int = 0, parent: int = None):
            """
            Pre-order traversal
            Update ans to be the answer by combining the count of itself and its parent
            """
            for child in graph[node]:
                if child != parent:
                    # Count of child + Count of parent (which is N - Count of child)
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
