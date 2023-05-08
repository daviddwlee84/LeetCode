from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        # Start from the leaves
        for i in range(n - 1, 0, -2):
            # Compare with its
            if cost[i - 1] > cost[i]:
                ans += cost[i - 1] - cost[i]
                cost[i] = cost[i - 1]
            else:
                ans += cost[i] - cost[i - 1]
                cost[i - 1] = cost[i]

            # Update parent node (for sum of the paths)
            cost[(i - 1) // 2] += cost[i]

        return ans
