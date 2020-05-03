from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        # first collect some candidates
        # (sum, index 1, index 2)
        result = []
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        heapq.heapify(heap)

        # colon equel (:=) is a python 3.8 feature
        # [What does colon equal (:=) in Python mean? - Stack Overflow](https://stackoverflow.com/questions/26000198/what-does-colon-equal-in-python-mean)
        while heap and (k := k-1) >= 0:
            _, i1, i2 = heapq.heappop(heap)
            result.append([nums1[i1], nums2[i2]])

            if i2 + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i1] + nums2[i2+1], i1, i2+1))

        return result

# Runtime: 44 ms, faster than 94.30% of Python3 online submissions for Find K Pairs with Smallest Sums.
# Memory Usage: 14.1 MB, less than 33.33% of Python3 online submissions for Find K Pairs with Smallest Sums.
