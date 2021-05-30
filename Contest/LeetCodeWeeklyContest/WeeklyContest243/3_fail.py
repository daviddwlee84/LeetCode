from typing import List
import heapq
from collections import defaultdict


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        server_heap = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(server_heap)
        server_free = defaultdict(list)

        ans = []
        time = 0
        for duration in tasks:
            while server_free[time]:
                i = server_free[time].pop()
                weight = servers[i]
                heapq.heappush(server_heap, (weight, i))

            if server_heap:
                _, server_i = heapq.heappop(server_heap)
                ans.append(server_i)
                server_free[time + duration].append(server_i)

            time += 1

        return ans

# WA
# servers: [10,63,95,16,85,57,83,95,6,29,71]
# tasks: [70,31,83,15,32,67,98,65,56,48,38,90,5]
#
# output: [8,0,3,9,5,1,10,6,4,2,7]
# expect: [8,0,3,9,5,1,10,6,4,2,7,9,0]
