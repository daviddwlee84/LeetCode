from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Alex Wice's solution
        """
        n = len(grid)
        right_zeros = []
        for row in grid:
            i = n
            while i - 1 >= 0 and row[i - 1] == 0:
                i -= 1
            right_zeros.append(n - i)

        swap_count = 0

        for requirement in range(n - 1, -1, -1):
            for i, zeros in enumerate(right_zeros):
                if zeros >= requirement:
                    swap_count += i
                    right_zeros.pop(i)
                    break
            else:
                return -1
        
        return swap_count
            