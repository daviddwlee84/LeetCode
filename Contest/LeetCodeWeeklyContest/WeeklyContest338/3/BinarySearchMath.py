from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []

        nums.sort()

        # To calculate sum of a section quickly
        cumulative_sum = [0]
        for num in nums:
            cumulative_sum.append(cumulative_sum[-1] + num)

        for q in queries:
            i = bisect_left(nums, q)
            temp = 0
            # Numbers smaller than q
            temp += q * i - cumulative_sum[i]
            # Numbers larger than q
            temp += (cumulative_sum[-1] -
                     cumulative_sum[i]) - q * (len(nums) - i)
            answer.append(temp)

        return answer
