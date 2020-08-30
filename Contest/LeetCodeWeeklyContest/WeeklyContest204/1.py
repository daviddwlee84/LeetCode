from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k > len(arr):
            return False

        for start in range(len(arr) - k * m + 1):
            pattern = arr[start:start + m] * k
            if arr[start:start + m * k] == pattern:
                return True

        return False


# [2,2]
# 1
# 2
