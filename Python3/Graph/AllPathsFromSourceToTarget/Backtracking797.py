from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/all-paths-from-source-to-target/discuss/118691/C%2B%2BPython-Backtracking

        Because this is directed, acyclic graph, so we don't need to record what node has been visited
        """

        answer = []
        def dfs(cur, path):
            if cur == len(graph) - 1:
                answer.append(path)
            else:
                for node in graph[cur]:
                    dfs(node, path + [node])
        dfs(0, [0])
        return answer

