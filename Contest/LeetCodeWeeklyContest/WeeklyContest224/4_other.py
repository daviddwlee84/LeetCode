from typing import List
import functools


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        """
        Alex Wice copied Lerry's Solution
        """
        MOUSE, CAT = 0, 1
        ROWS, COLS = len(grid), len(grid[0])
        # Store the global position of the mouse, cat and food
        POSITION = {}
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] in ['M', 'C', 'F']:
                    POSITION[grid[row][col]] = (row, col)

        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # https://docs.python.org/3/library/functools.html
        # This is new in Python 3.9
        @functools.cache
        def decide(mr, mc, cr, cc, turn):
            """
            This records the board states
            """
            if (mr, mc) == POSITION['F']:
                return MOUSE
            if (mr, mc) == (cr, cc):
                return CAT
            if (cr, cc) == POSITION['F']:
                return CAT
            if turn >= 80:
                return CAT

            # enumerate neighbors
            if turn & 1 == 0:  # mouse's turn
                for dr, dc in DIRECTIONS:
                    for k in range(mouseJump + 1):
                        nr = mr + dr * k  # next row
                        nc = mc + dc * k  # next col

                        if not (0 <= nr < ROWS and 0 <= nc < COLS):
                            # exceed the edge
                            break

                        if grid[nr][nc] == '#':
                            # step into the wall
                            break

                        if decide(nr, nc, cr, cc, turn + 1) == MOUSE:
                            return MOUSE

                return CAT
            else:  # cat's turn
                for dr, dc in DIRECTIONS:
                    for k in range(catJump + 1):
                        nr = cr + dr * k  # next row
                        nc = cc + dc * k  # next col

                        if not (0 <= nr < ROWS and 0 <= nc < COLS):
                            # exceed the edge
                            break

                        if grid[nr][nc] == '#':
                            # step into the wall
                            break

                        if decide(mr, mc, nr, nc, turn + 1) == CAT:
                            return CAT

                return MOUSE

        return decide(*POSITION['M'], *POSITION['C'], 0) == MOUSE
