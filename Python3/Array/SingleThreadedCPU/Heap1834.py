from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = [(enqueueTime, processingTime, i)
                 for i, (enqueueTime, processingTime) in enumerate(tasks)]
        # tasks = [(i[1][0], i[1][1], i[0])
        #          for i in sorted(enumerate(tasks), key=lambda x: (x[1][0]))]
        # tasks.sort(key=lambda x: (x[0], x[2]))
        tasks.sort(key=lambda x: x[0])

        i = 0
        time = 1
        heap = []
        order = []
        occupied = -1
        while i < len(tasks) or heap:

            # 1. Add job to queue
            while i < len(tasks) and tasks[i][0] == time:
                # (processingTime, index)
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            # print(i, time, occupied, heap)

            # 2. Choose job to execute or run
            if occupied <= 0 and heap:
                to_run = heapq.heappop(heap)
                occupied = to_run[0]
                order.append(to_run[1])

            time += 1
            occupied -= 1

        # print(order)
        return order
