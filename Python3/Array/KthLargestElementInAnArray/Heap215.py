from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, -num)
        # for _ in range(k):
        #     temp = heapq.heappop(heap)
        # return -temp

        # equivalent
        heapq._heapify_max(nums)
        for _ in range(k):
            temp = heapq._heappop_max(nums)

        return temp