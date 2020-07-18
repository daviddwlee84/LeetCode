from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/solution/
        """
        if k == len(nums):
            return nums

        # build hash map
        # O(N)
        count = Counter(nums)

        # build heap of top k frequent elements
        # and convert it into an output array
        # O(Nlogk)
        return heapq.nlargest(k, count.keys(), key=count.get)
