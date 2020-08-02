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

        row_zero_count = []

        for row in grid:
            zero_count = count_right_zeros(row)
            row_zero_count.append(zero_count)

        # Check if this problem is solvable
        for zero_count, at_least in zip(sorted(row_zero_count)[-n + 1:], range(1, n)):
            if zero_count < at_least:
                return -1

        # Find start sorting point
        start_sort = -1
        for i in range(n):
            #print(row_zero_count[i], n - 1 - i)
            if row_zero_count[i] < n - 1 - i:
                start_sort = i
                break
            if i == n - 1:
                start_sort = n - 1

        # print(start_sort)

        swap_count = 0
        for i in range(n - start_sort):
            for j in range(n - 1, i + start_sort, -1):
                # print(j)
                if row_zero_count[j] > row_zero_count[j - 1]:
                    row_zero_count[j], row_zero_count[j -
                                                      1] = row_zero_count[j - 1], row_zero_count[j]
                    swap_count += 1
        # print(row_zero_count)

        return swap_count

# WA
# [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
# [[1,0,0,0,0,0],
#  [0,1,0,1,0,0],
#  [1,0,0,0,0,0],
#  [1,1,1,0,0,0],
#  [1,1,0,1,0,0],
#  [1,0,0,0,0,0]]
# 2
