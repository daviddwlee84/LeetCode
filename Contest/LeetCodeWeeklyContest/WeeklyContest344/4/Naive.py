from typing import List
from collections import deque, defaultdict


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        """
        Wrong Answer

        15
        [764,1460,2664,764,2725,4556,5305,8829,5064,5929,7660,6321,4830,7055,3761]

        Output: 30257
        Expected: 15735
        """
        level_costs = defaultdict(int)

        # node, level
        queue = deque([(1, 0)])

        # Find the max level cost
        while queue:
            node, level = queue.pop()
            level_costs[level] = max(cost[node - 1], level_costs[level])

            if 2 * node < n:
                # left child
                queue.appendleft((2 * node, level + 1))
                # right child
                queue.appendleft((2 * node + 1, level + 1))

        # print(level_costs)
        ans = 0
        queue = deque([(1, 0)])
        while queue:
            node, level = queue.pop()
            ans += level_costs[level] - cost[node - 1]
            if 2 * node < n:
                # left child
                queue.appendleft((2 * node, level + 1))
                # right child
                queue.appendleft((2 * node + 1, level + 1))
        return ans
