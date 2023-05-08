from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        left = 0
        right = len(mat) - 1
        for row in mat:
            if left == right:
                ans += row[left]
            else:
                ans += row[left] + row[right]
            left += 1
            right -= 1
        return ans
