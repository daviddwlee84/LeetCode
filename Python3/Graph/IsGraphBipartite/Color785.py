from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        https://leetcode.com/problems/is-graph-bipartite/discuss/115487/Java-Clean-DFS-solution-with-Explanation
        https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution

        DFS with node coloring

        node not in color: haven't been colored yet
        node is -1: color 1
        node is 1: color 2 
        """
        self.colors = {}  # visited nodes with color

        def validColor(node: int, to_color: int) -> bool:
            if self.colors.get(node, False):
                return self.colors[node] == to_color

            self.colors[node] = to_color

            for neighbour in graph[node]:
                if not validColor(neighbour, -to_color):
                    return False

            return True

        for node in range(len(graph)):
            if node not in self.colors and not validColor(node, 1):
                return False

        return True


# Runtime: 168 ms, faster than 91.08 % of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 14.8 MB, less than 54.81 % of Python3 online submissions for Is Graph Bipartite?.
