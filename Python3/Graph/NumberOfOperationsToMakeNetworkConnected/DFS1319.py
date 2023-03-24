from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-operations-to-make-network-connected/solutions/3330355/python-simple-solution-easy-to-understand/
        """
        if len(connections) < n - 1:
            # Impossible to connect
            return -1

        graph = [set() for i in range(n)]
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()

        def dfs(node: int):
            # If node in visited means already count that group
            if node in visited:
                return 0

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

            return 1

        # We count how many group of computer
        # and we will need group - 1 times to reconnect them
        return sum(dfs(node) for node in range(n)) - 1
