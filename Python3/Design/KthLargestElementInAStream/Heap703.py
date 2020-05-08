from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/615345/Simple-python-priority-queue-MinHeap-solution
        """
        self.minHeap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            # just maintain k largest item
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Runtime: 80 ms, faster than 99.92% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 17.5 MB, less than 8.70% of Python3 online submissions for Kth Largest Element in a Stream.
