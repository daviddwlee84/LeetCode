from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        num_sum = sum(nums) / 4
        answer = []
        for q in queries:
            answer.append(num_sum - q * len(nums))
        return answer
