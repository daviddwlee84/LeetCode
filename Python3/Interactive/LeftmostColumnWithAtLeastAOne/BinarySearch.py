# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        result = float('inf')

        # For each row, binary search to find the left most 1
        for i in range(n):
            left, right = 0, m
            while left < right:
                # mid = (left + right) // 2
                mid = left + (right - left) // 2
                if binaryMatrix.get(i, mid) == 0:
                    left = mid + 1
                else:
                    right = mid

            # If found one, then update the result
            if left < m and binaryMatrix.get(i, left) == 1:
                result = min(result, left)

        return result if result != float('inf') else -1
