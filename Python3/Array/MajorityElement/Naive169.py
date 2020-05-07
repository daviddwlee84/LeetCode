from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        majority_count = len(nums) // 2

        for num in nums:
            count[num] += 1
            if count[num] > majority_count:
                return num

# Runtime: 192 ms, faster than 23.83% of Python3 online submissions for Majority Element.
# Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.
