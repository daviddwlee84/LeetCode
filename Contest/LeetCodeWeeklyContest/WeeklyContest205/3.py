from itertools import groupby


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 0
        ans = 0
        for char, groups in groupby(s):
            groups = list(groups)
            if len(groups) > 1:
                ans += sum(cost[i:i + len(groups)]) - \
                    max(cost[i:i + len(groups)])
            i += len(groups)

        return ans
