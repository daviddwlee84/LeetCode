from typing import List
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_count = Counter(map(lambda x: x % k, arr))

        if mod_count[0] % 2 != 0:
            return False

        for i in range(1, k // 2):
            if mod_count[i] != mod_count[k - i]:
                return False

        return True
