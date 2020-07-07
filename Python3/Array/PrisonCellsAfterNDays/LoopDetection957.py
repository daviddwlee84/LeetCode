from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        https://leetcode.com/problems/prison-cells-after-n-days/discuss/717491/Python-Loop-detection-explained
        https://leetcode.com/problems/prison-cells-after-n-days/discuss/717989/Three-Solutions-with-Detailed-Explanation
        """
        found_dict = {}
        for day in range(N):
            cells_str = str(cells)

            if cells_str in found_dict:
                # found loop, directly calculate final state
                # (actually, loop_len will always have length 14 or divisor of it)
                loop_len = day - found_dict[cells_str]
                return self.prisonAfterNDays(cells, (N - day) % loop_len)
            else:
                found_dict[cells_str] = day
                cells = self.get_next_day(cells)

        # if haven't reach any loop
        return cells

    def get_next_day(self, cells: List[int]) -> List[int]:
        next_cells = [0] * 8
        for i in range(1, 7):
            next_cells[i] = int(cells[i - 1] == cells[i + 1])

        return next_cells

# Runtime: 80 ms, faster than 5.13% of Python3 online submissions for Prison Cells After N Days.
# Memory Usage: 13.9 MB, less than 30.61% of Python3 online submissions for Prison Cells After N Days.
