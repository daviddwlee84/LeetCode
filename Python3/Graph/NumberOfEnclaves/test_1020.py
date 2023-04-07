from DFS1020 import Solution as DFS

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
