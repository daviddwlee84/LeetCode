from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2  # total 2N

        # First half is best for A, the second half is best for B
        costs.sort(key=lambda cost: cost[0] - cost[1])

        total_cost = 0
        for i in range(N):
            total_cost += costs[i][0] + costs[i+N][1]

        return total_cost

# Runtime: 32 ms, faster than 97.08% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.7 MB, less than 7.69% of Python3 online submissions for Two City Scheduling.
