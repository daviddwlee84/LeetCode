from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the following three lines are equivalent to
        # collections.Counter(nums)
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1

        # the following lines are equivalent to
        # heapq.nlargest(k, hash_table.keys(), key=hash_table.get)
        heap = list(hash_table.values())
        heapq._heapify_max(heap)
        ans = []
        for _ in range(k):
            largest = heapq._heappop_max(heap)
            for num, freq in hash_table.items():
                if freq == largest:
                    ans.append(num)
                    hash_table.pop(num)
                    break
        return ans
