from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        LHS = 0
        last_num_freq = None
        for num, freq in sorted(Counter(nums).items(), key=lambda item: item[0]):
            if not last_num_freq:
                last_num_freq = (num, freq)
                continue

            if num - last_num_freq[0] == 1:
                LHS = max(LHS, freq + last_num_freq[1])

            last_num_freq = (num, freq)

        return LHS
