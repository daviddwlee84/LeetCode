from typing import List
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_idx = defaultdict(set)
        for i, num in enumerate(nums):
            num_idx[num].add(i)

        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            for j in num_idx[num]:
                ans[i] += abs(i - j)
        return ans
