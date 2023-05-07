from typing import List
from collections import defaultdict


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix_count = defaultdict(int)
        prefix = []
        suffix_count = defaultdict(int)
        suffix = []
        for num in nums:
            prefix_count[num] += 1
            prefix.append(len(prefix_count))

        for num in reversed(nums):
            suffix.append(len(suffix_count))
            suffix_count[num] += 1

        # print(prefix, suffix)
        ans = []
        for p, s in zip(prefix, reversed(suffix)):
            ans.append(p - s)

        return ans
