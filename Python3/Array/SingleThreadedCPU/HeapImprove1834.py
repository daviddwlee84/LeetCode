from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = [(enqueueTime, processingTime, i)
                 for i, (enqueueTime, processingTime) in enumerate(tasks)]
        tasks.sort(key=lambda x: x[0])

        i = 0
        time = 0
        heap = []
        order = []
        while i < len(tasks) or heap:
            # 0. Skip to speed up
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # print(i, time, heap)

            # 1. Add job to queue
            while i < len(tasks) and tasks[i][0] <= time:
                # (processingTime, index)
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            # 2. Choose job to execute or run
            processingTime, index = heapq.heappop(heap)
            order.append(index)

            time += processingTime

        return order
