from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """ https://leetcode.com/problems/two-city-scheduling/discuss/667781/Python-3-Lines-O(n-log-n)-with-sort-explained """
        city_A_cost = 0
        diff = []

        for costA, costB in costs:
            diff.append(costB - costA)
            city_A_cost += costA

        return city_A_cost + sum(sorted(diff)[:len(costs)//2])

# Runtime: 36 ms, faster than 90.00% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Two City Scheduling.
