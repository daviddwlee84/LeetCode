from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def count_right_zeros(row: List[int]) -> int:
            count = 0
            for i in reversed(range(n)):
                if row[i] == 0:
                    count += 1
                else:
                    break
            return count

        right_zeros = []

        for row in grid:
            zero_count = count_right_zeros(row)
            right_zeros.append(zero_count)

        swap_count = 0

        for i in range(n):
            if right_zeros[i] < n - 1 - i:
                # find a fit one and do bubble sort
                for j in range(i + 1, n + 1):
                    if j == n:
                        return -1
                    if right_zeros[j] >= n - 1 - i:
                        break

                for k in range(j, i, -1):
                    swap_count += 1
                    right_zeros[k], right_zeros[k -
                                                1] = right_zeros[k - 1], right_zeros[k]

        return swap_count
