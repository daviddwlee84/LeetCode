from typing import List
from itertools import combinations, product


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        answer = len(nums)
        for i in range(2, len(nums) + 1):
            for comb in combinations(nums, i):
                is_beautiful = True
                for num1, num2 in product(comb, comb):
                    if abs(num1 - num2) == k:
                        is_beautiful = False
                        break
                answer += is_beautiful
    
        return answer

# TLE
# [15,6,3,25,14,29,21,16,28,23,11,9,4,30,24,12,26,1,27,18]
# 7
