from typing import List
import heapq


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        answer = []
        
        while nums:
            answer.append(heapq.heappop(nums))
        
        return answer
