from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq._heapify_max(stones)

        if not stones:
            return 0

        heap_stones = []
        for stone in stones:
            # max heap
            heapq.heappush(heap_stones, -stone)

        while len(heap_stones) > 1:
            y = -heapq.heappop(heap_stones)
            x = -heapq.heappop(heap_stones)

            if x != y:
                heapq.heappush(heap_stones, -(y - x))

        if heap_stones:
            return -heap_stones[0]
        else:
            return 0
