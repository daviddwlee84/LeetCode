from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        This will TLE
        32 / 35 testcases passed
        """
        project_used = set()
        while k:
            temp_p = 0
            temp_i = -1
            for i, (p, c) in enumerate(zip(profits, capital)):
                if i in project_used:
                    continue
                if c <= w and p > temp_p:
                    temp_p = p
                    temp_i = i
            project_used.add(temp_i)
            w += temp_p
            k -= 1

        return w
