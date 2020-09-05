from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        https://youtu.be/-IPzqZeVmr4?t=755
        """
        result = []
        b_count = Counter()
        for b in B:
            for char, cnt in Counter(b).items():
                b_count[char] = max(b_count[char], cnt)

        for a in A:
            a_count = Counter(a)
            if all(a_count[char] >= b_count[char] for char in b_count):
                result.append(a)

        return result

# Runtime: 916 ms, faster than 71.29% of Python3 online submissions for Word Subsets.
# Memory Usage: 17.4 MB, less than 86.13% of Python3 online submissions for Word Subsets.
