from typing import List
import heapq
from fractions import Fraction


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        minCost = float('inf')
        # to make a min heap be max heap, just multiply -1 for each value when adding
        maxHeap_quality = []

        # ordering workers with the ratio
        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))
        qualitySum = 0

        for ratio, q, w in workers:
            heapq.heappush(maxHeap_quality, -q)
            qualitySum += q

            if len(maxHeap_quality) > K:
                # pop the candidate with the max quality
                # (don't forget to take the negative sign)
                qualitySum -= -heapq.heappop(maxHeap_quality)

            if len(maxHeap_quality) == K:
                # update possible answer
                minCost = min(minCost, ratio * qualitySum)

        return minCost

# Runtime: 1208 ms, faster than 14.25% of Python3 online submissions for Minimum Cost to Hire K Workers.
# Memory Usage: 15.6 MB, less than 25.00% of Python3 online submissions for Minimum Cost to Hire K Workers.
