from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        set_size = 0
        total = 0
        for _, cnt in counter.most_common():
            total += cnt
            set_size += 1
            if total >= len(arr) / 2:
                break
        return set_size
