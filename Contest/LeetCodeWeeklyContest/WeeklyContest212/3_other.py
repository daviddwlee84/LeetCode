from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Alex Wice's Solution

        Trick: binary search for the answer

        Time Complexity O(rows * cols log W)
        """

        rows = len(heights)
        cols = len(heights[0])

        def possible(effort: int) -> bool:
            stack = [(0, 0)]
            seen = {(0, 0)}
            while stack:
                row, col = stack.pop()
                if row == rows - 1 and col == cols - 1:
                    return True

                for next_row, next_col in ((row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)):
                    if (
                        0 <= next_row < rows and 0 <= next_col < cols
                        and abs(heights[next_row][next_col] - abs(heights[row][col])) <= effort and
                        (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))

        low, high = 0, 10 ** 6

        while low < high:
            mid = low + high >> 1
            if not possible(mid):
                low = mid + 1
            else:
                high = mid

        return low

# Runtime: 1816 ms, faster than 50.00% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 15.9 MB, less than 50.00% of Python3 online submissions for Path With Minimum Effort.
