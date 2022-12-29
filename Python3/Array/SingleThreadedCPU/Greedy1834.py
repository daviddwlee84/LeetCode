from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # https://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python
        # Wrong idea
        # return [i[0] for i in sorted(enumerate(tasks), key=lambda x: (x[1][1], x[1][0]))]
        tasks.sort(key=lambda x: x[0])

        i = 0
        time = 1
        queue = []
        order = []
        occupied = -1
        while i < len(tasks) or queue:

            # 1. Add job to queue
            while i < len(tasks) and tasks[i][0] == time:
                queue.append((tasks[i][1], i))
                i += 1

            # 2. Choose job to execute or run
            if occupied <= 0 and queue:
                to_run = min(queue)
                queue.remove(to_run)
                occupied = to_run[0]
                order.append(to_run[1])

            time += 1
            occupied -= 1

        return order
