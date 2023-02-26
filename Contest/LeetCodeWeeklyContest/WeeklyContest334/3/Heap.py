from typing import List
import heapq

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        min_heap = nums.copy()
        heapq.heapify(min_heap)
        max_num = max(nums)

        answer = 0
        while min_heap:
            min_val = heapq.heappop(min_heap)
            if min_val * 2 <= max_num:
                answer += 1
            else:
                break
        return answer

# WA
# [1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10]
# output: 35
# expected: 64
