from typing import List
import heapq
from collections import defaultdict, deque


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        server_heap = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(server_heap)
        server_free = defaultdict(list)
        pending = deque()

        ans = [None] * len(tasks)
        time = 0
        while time < len(tasks) or pending:
            duration = None
            if time < len(tasks):
                # release new tasks
                task_i = time
                duration = tasks[time]
                pending.append((duration, task_i))

            if server_free[time]:
                for i in server_free[time]:
                    weight = servers[i]
                    heapq.heappush(server_heap, (weight, i))
                del server_free[time]

            while server_heap and pending:
                duration, task_i = pending.popleft()
                _, server_i = heapq.heappop(server_heap)
                ans[task_i] = server_i
                server_free[time + duration].append(server_i)

            time += 1

        return ans


# TLE
