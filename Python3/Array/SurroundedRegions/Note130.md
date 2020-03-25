# 130. Surrounded Regions

## Description

Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example**:

```txt
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```txt
X X X X
X X X X
X X X X
X O X X
```

**Explanation**:

Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## Solution

## Others' Solution

```py
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        nr, nc = len(board), len(board[0])

        def dfs(y, x):
            if y < 0 or y >= nr or x < 0 or x >= nc:
                return
            if board[y][x] == "X":
                return
            if board[y][x] == "O":
                board[y][x] = "."
                for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    dfs(y + dy, x + dx)
        for y in range(nr):
            dfs(y, 0)
            dfs(y, nc - 1)
        for x in range(nc):
            dfs(0, x)
            dfs(nr - 1, x)
        for y in range(nr):
            for x in range(nc):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == ".":
                    board[y][x] = "O"
```
