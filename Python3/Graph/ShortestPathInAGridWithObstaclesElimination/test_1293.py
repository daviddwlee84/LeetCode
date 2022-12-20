from BFS1293 import Solution as BFS

testcases = [
    ([[0, 0, 0],
      [1, 1, 0],
      [0, 0, 0],
      [0, 1, 1],
      [0, 0, 0]], 1, 6),
    ([[0, 1, 1],
      [1, 1, 1],
      [1, 0, 0]], 1, -1),
    ([[0, 0],
      [1, 0],
      [1, 0],
      [1, 0],
      [1, 0],
      [1, 0],
      [0, 0],
      [0, 1],
      [0, 1],
      [0, 1],
      [0, 0],
      [1, 0],
      [1, 0],
      [0, 0]], 4, 14),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], 1, 20),
    ([[0]], 1, 0),
]


def test_BFS():
    for grid, k, ans in testcases:
        assert BFS().shortestPath(grid, k) == ans