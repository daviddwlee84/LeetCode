from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        answer = mat[0]
        for i in range(1, len(mat)):
            answer = self.kSmallestPairs(answer, mat[i], 200)
        
        return answer[k-1]


    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """ copy paste from Python3/Array/FindKPairsWithSmallestSums/PriorityQueue373.py (modify the return) """
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
            sum_of_num12, num1, _, idx2 = heapq.heappop(heap)
            result.append(sum_of_num12)
            k -= 1

            if idx2 == len(nums2) - 1:
                continue

            heapq.heappush(heap, (num1 + nums2[idx2 + 1], num1, nums2[idx2+1], idx2+1))

        return result

# Runtime: 416 ms, faster than 18.18% of Python3 online submissions for Find the Kth Smallest Sum of a Matrix With Sorted Rows.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Find the Kth Smallest Sum of a Matrix With Sorted Rows.
