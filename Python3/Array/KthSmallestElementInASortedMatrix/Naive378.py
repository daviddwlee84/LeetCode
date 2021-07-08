from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = [cell for row in matrix for cell in row]
        return sorted(array)[k - 1]

# Runtime: 168 ms, faster than 80.33% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 78.24% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
