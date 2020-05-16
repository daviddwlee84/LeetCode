from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """ brute force """

        global_max = float('-inf')
        for window_size in range(1, len(A) + 1):
            for start in range(len(A)):
                if start + window_size < len(A):
                    temp = sum(A[start: start + window_size])
                else:
                    temp = sum(A[start:] + A[:start + window_size - len(A)])
                global_max = max(global_max, temp)

        return global_max

# TLE
