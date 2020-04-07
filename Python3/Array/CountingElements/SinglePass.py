from typing import List
from collections import defaultdict


class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_table = defaultdict(int)

        result = 0
        for a in arr:
            if a + 1 in hash_table:
                result += 1
            if a not in hash_table and a - 1 in hash_table:
                result += hash_table[a - 1]

            hash_table[a] += 1

        return result
