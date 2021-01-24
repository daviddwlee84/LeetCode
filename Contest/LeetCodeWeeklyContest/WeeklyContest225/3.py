from typing import List
from functools import cache
import heapq


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        @cache
        def xor(a: int, b: int):
            """
            2D prefix sum
            """
            if a == 0 and b == 0:
                return matrix[a][b]
            elif a == 0:
                return xor(a, b - 1) ^ matrix[a][b]
            elif b == 0:
                return xor(a - 1, b) ^ matrix[a][b]
            else:
                # ^ xor(a - 1, b - 1) is used to recover the duplicate part
                return xor(a, b - 1) ^ xor(a - 1, b) ^ matrix[a][b] ^ xor(a - 1, b - 1)

        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heap.append(xor(i, j))

        return heapq.nlargest(k, heap)[-1]
