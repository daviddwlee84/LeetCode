from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []

        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return result

        i = 0
        # just collect some candidate from all number in nums1 (at most k)
        while i < len(nums1) and i < k:
            # sum of all nums1 with nums2 smallest number
            # (sum, nums1 number, nums2 number, nums2 index)
            heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
            i += 1

        while k > 0 and heap:
            _, num1, num2, idx2 = heapq.heappop(heap)
            result.append([num1, num2])
            k -= 1

            if idx2 == len(nums2) - 1:
                continue

            heapq.heappush(heap, (num1 + nums2[idx2 + 1], num1, nums2[idx2+1], idx2+1))

        return result

# Runtime: 40 ms, faster than 98.88% of Python3 online submissions for Find K Pairs with Smallest Sums.
# Memory Usage: 14 MB, less than 33.33% of Python3 online submissions for Find K Pairs with Smallest Sums.


# if use 
#           if idx2 < len(nums2) - 1:
#               heapq.heappush(heap, (num1 + nums2[idx2 + 1], num1, nums2[idx2+1], idx2+1))
#
# Runtime: 84 ms, faster than 46.39% of Python3 online submissions for Find K Pairs with Smallest Sums.
# Memory Usage: 14 MB, less than 33.33% of Python3 online submissions for Find K Pairs with Smallest Sums.