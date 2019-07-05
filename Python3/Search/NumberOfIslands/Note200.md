# 200. Number of Islands

## Descripiton

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1**:

```txt
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2**:

```txt
Input:
11000
11000
00100
00011

Output: 3
```

## Solution

### BFS

### DFS

## Other's solution

### BFS using deque

```py
'''
grid of 1s and 0s
1 = land
0 = water

connected (4-way) land -- island
surrounded by water

11000
11000
00100
00011

BFS or DFS
this of it as a graph, neighbors are connected by edges
start from one point (top-left)
expand, label nodes as visited


'''

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        nrow = len(grid)
        ncol = len(grid[0])

        delta = [(0,1), (0,-1), (1,0), (-1,0)]

        visited = set()

        n_island = 0

        for x in range(nrow):
            for y in range(ncol):
                if (x, y) in visited or grid[x][y] == '0':
                    continue

                n_island += 1

                q = deque()
                q.append((x,y))

                while len(q) != 0:
                    prev_i, prev_k = q.pop()
                    visited.add((prev_i, prev_k))

                    for di, dk in delta:
                        i, k = prev_i + di, prev_k + dk
                        if i < 0 or i >= nrow or k < 0 or k >= ncol:
                            continue

                        if grid[i][k] == '0':
                            continue

                        if (i, k) not in visited:
                            q.append((i, k))

        return n_island
```

### union

```py

from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.grid = None
        self.sets = None
        self.parent = [0]

    def find(self, k):
        i = k
        while self.parent[i] != i:
            i = self.parent[i]
        self.parent[k] = i
        return i

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        self.parent[i] = j
        return j

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        m = len(grid[0])

        self.grid = grid
        sets = self.sets = [[0]*m for i in range(n)]

        sequence = 1
        cur = [0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    cur[j] = 0
                    continue

                left = cur[j-1] if j > 0 else 0
                top = cur[j]
                if not left and not top:
                    cur[j] = sequence
                    self.parent.append(sequence)
                    sequence += 1
                elif left and not top:
                    cur[j] = left
                elif not left and top:
                    cur[j] = top
                else:
                    cur[j] = self.union(left, top)

        return sum(1 for i in range(1, len(self.parent)) if self.parent[i] == i)
```
