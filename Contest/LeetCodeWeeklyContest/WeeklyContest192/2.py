from typing import List
import heapq


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        candidate = []

        for num in arr:
            score = abs(num - median)
            heapq.heappush(candidate, (score, num))

        answer = heapq.nlargest(k, candidate)
        return [num for _, num in answer]
