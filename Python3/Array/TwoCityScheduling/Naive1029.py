from typing import List
import heapq

# https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A = []
        B = []

        # Everyone first choose low cost city
        for i, cost in enumerate(costs):
            if cost[0] < cost[1]:
                heapq.heappush(A, (cost[1] - cost[0], cost[0], i))
            else:
                heapq.heappush(B, (cost[0] - cost[1], cost[1], i))

        # Adjust if the number is not balance
        while len(A) != len(B):
            if len(A) > len(B):
                _, _, i = heapq.heappop(A)
                heapq.heappush(B, (costs[i][0] - costs[i][1], costs[i][1], i))
            else:
                _, _, i = heapq.heappop(B)
                heapq.heappush(A, (costs[i][1] - costs[i][0], costs[i][0], i))

        return sum([cost for _, cost, _ in A]) + sum([cost for _, cost, _ in B])

# Runtime: 44 ms, faster than 50.31% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 14 MB, less than 7.69% of Python3 online submissions for Two City Scheduling.
