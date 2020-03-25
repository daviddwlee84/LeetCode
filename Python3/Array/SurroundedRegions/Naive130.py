from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # if not reach the edge, then they should be warp in X

        if not board:
            return board

        self.m, self.n = len(board), len(board[0])

        self.visited = set()

        for i in range(self.m):
            for j in range(self.n):
                # if found O then start travel
                if board[i][j] == 'O' and (i, j) not in self.visited:
                    region, reach_edge = self.dfs(board, i, j)
                    if not reach_edge:
                        self.flip(board, region)

        return board

    def dfs(self, board: List[List[str]], i, j):
        """
        Collect all stuff in the same region, 
        """
        stack = [(i, j)]
        region = []
        reach_edge = False
        while stack:
            next_visit = stack.pop()
            if next_visit[0] in (0, self.m-1) or next_visit[1] in (0, self.n-1):
                reach_edge = True
            self.visited.add(next_visit)
            region.append(next_visit)

            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= next_visit[0] + direction[0] < self.m and 0 <= next_visit[1] + direction[1] < self.n:
                    # if index is valid
                    temp_index = (
                        next_visit[0] + direction[0], next_visit[1] + direction[1])
                    if board[temp_index[0]][temp_index[1]] == 'O' and temp_index not in self.visited:
                        stack.append(temp_index)
        return region, reach_edge

    def flip(self, board: List[List[str]], to_flip):
        """
        Set O to X
        """
        for i, j in to_flip:
            board[i][j] = 'X'

# Runtime: 352 ms, faster than 6.21% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 21.6 MB, less than 6.67% of Python3 online submissions for Surrounded Regions.
