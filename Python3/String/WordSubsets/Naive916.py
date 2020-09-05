from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result = []
        for a in A:
            a_count = Counter(a)

            found = True
            for b in B:
                a_temp = a_count.copy()
                for char, cnt in Counter(b).items():
                    if char not in a_temp or a_temp[char] < cnt:
                        found = False
                        break

            if found:
                result.append(a)

        return result

# TLE
# https://leetcode.com/submissions/detail/391279487/testcase/

