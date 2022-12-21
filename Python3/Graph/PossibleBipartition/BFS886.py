from typing import List
from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(source):
            q = deque([source])
            color[source] = 0  # Start with marking source as 'RED'
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    # If there is a conflict, return false.
                    if color[neighbor] == color[node]:
                        return False

                    # Unvisited
                    if color[neighbor] == -1:
                        # Assign the flip of current color
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)

            return True

        # Note that, the adj[0] is dummy
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)  # 0 stands for red and 1 stands for blue.
        # Make sure all the nodes have color
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run BFS.
                if not bfs(i):
                    # Return false, if there is conflict in the component.
                    return False

        return True
