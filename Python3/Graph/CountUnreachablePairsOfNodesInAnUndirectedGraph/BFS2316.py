from typing import List
from collections import defaultdict, deque


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        group_sizes = []
        for i in range(n):
            if i in visited:
                continue
            count = 0
            queue = deque([i])
            visited.add(i)
            while queue:
                x = queue.pop()
                count += 1
                # print(x)
                for neigh in graph[x]:
                    if neigh not in visited:
                        visited.add(neigh)
                        # print(x, neigh)
                        queue.appendleft(neigh)
            group_sizes.append(count)

        # print(group_sizes)

        answer = 0
        first_group_size = group_sizes[0]
        for i in range(1, len(group_sizes)):
            answer += first_group_size * group_sizes[i]
            first_group_size += group_sizes[i]
        return answer
