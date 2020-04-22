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
        # Start from the bottom right
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                # Move up
                i -= 1
            else:
                # Move left
                j -= 1

        return - 1 if j == m - 1 else j + 1
