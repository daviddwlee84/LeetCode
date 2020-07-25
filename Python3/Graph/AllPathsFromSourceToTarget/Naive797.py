from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        https://www.geeksforgeeks.org/find-paths-given-source-destination/
        """
        self.graph = graph
        self.destination = len(graph) - 1
        visited = [False] * len(graph)
        self.answer = []

        self.dfs(0, [], visited)
        return self.answer

    def dfs(self, curr_node, path, visited):
        visited[curr_node] = True
        path.append(curr_node)
        if curr_node == self.destination:
            self.answer.append(path.copy())
        else:
            for next_node in self.graph[curr_node]:
                if not visited[next_node]:
                    self.dfs(next_node, path, visited)
        visited[curr_node] = False
        path.pop()
