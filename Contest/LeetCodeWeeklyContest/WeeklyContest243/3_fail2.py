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
        while time < len(tasks) or server_free:
            duration = None
            if time < len(tasks):
                # release new tasks
                duration = tasks[time]

            if server_free[time]:
                for i in server_free[time]:
                    weight = servers[i]
                    heapq.heappush(server_heap, (weight, i))
                del server_free[time]

            if server_heap and duration is not None:
                _, server_i = heapq.heappop(server_heap)
                ans.append(server_i)
                server_free[time + duration].append(server_i)

            time += 1

        return ans

# MLE
