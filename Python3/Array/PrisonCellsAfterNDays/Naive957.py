from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        for day in range(N):
            next_cells = []
            for i in range(8):

                if i - 1 >= 0:
                    if cells[i - 1] == 1:
                        left_occupied = True
                    else:
                        left_occupied = False
                else:
                    # (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
                    left_occupied = None

                if i + 1 < 8:
                    if cells[i + 1] == 1:
                        right_occupied = True
                    else:
                        right_occupied = False
                else:
                    # (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
                    right_occupied = None

                if left_occupied is None or right_occupied is None or (left_occupied ^ right_occupied):
                    next_cells.append(0)
                else:
                    next_cells.append(1)

            cells = next_cells

        return cells

# TLE
# [1,0,0,1,0,0,1,0]
# 1000000000
