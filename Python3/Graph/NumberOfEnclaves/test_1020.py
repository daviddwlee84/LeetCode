from DFS1020 import Solution as DFS
from SimplerDFS1020 import Solution as SimplerDFS

testcases = [
    ([[0, 0, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]], 3),
    ([[0, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0]], 0),
]


def test_DFS():
    for grid, ans in testcases:
        assert DFS().numEnclaves(grid) == ans


def test_SimplerDFS():
    for grid, ans in testcases:
        assert SimplerDFS().numEnclaves(grid) == ans
