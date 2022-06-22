from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        # return heapq.nlargest(k, heap)[-1]

        return heapq.nlargest(k, nums)[-1]
