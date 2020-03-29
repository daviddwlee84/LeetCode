from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_match = -1
        for num, count in Counter(arr).items():
            if num == count and num > max_match:
                max_match = num

        return max_match
