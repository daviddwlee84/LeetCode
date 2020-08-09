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
        candidates = []
        for i, cut in enumerate(cuts_to_consider):
            dis = abs(cut - mid)
            if dis < distance:
                candidates = [(cut, i)]
                distance = dis
            elif dis == distance:
                candidates.append((cut, i))

        mid_length = (len(cuts_to_consider) + 1) / 2
        distance = float('inf')
        for cut, i in candidates:
            dis = abs(i - mid_length)
            if dis < distance:
                best_cut = cut
                best_i = i
                distance = dis

        self.findClosestMid(start, best_cut, cuts_to_consider[:best_i])
        self.findClosestMid(best_cut, end, cuts_to_consider[best_i+1:])

# WA
# 7
# [1,3,4,5]
#
# 16 (17) (3 vs. 4, 1 vs. 3)
#
# 9
# [5,6,1,4,2]
#
# 22 (23) (4 vs. 5)
