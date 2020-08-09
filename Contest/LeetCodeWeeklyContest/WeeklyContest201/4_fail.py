from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cost = 0
        self.findClosestMid(0, n, sorted(cuts))
        return self.cost

    def findClosestMid(self, start: int, end: int, cuts_to_consider: List[int]):
        if len(cuts_to_consider) == 0:
            return

        self.cost += end - start

        mid = (start + end) / 2
        distance = float('inf')
        for i, cut in enumerate(cuts_to_consider):
            dis = abs(cut - mid)
            if dis < distance:
                best_cut = cut
                best_i = i
                distance = dis

        self.findClosestMid(start, best_cut, cuts_to_consider[:best_i])
        self.findClosestMid(best_cut, end, cuts_to_consider[best_i+1:])

# WA
# 20
# [1,14,18,6,17,8,10,4,13,16,7]
#
# 71 (72) => 4 vs. 6 (split at 5)
