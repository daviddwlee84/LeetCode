from BFS2492 import Solution as BFS
from UnionFind2492 import Solution as UnionFind

testcases = [
    (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
    (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
    (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 2]], 2),
]


def test_BFS():
    for n, roads, ans in testcases:
        assert BFS().minScore(n, roads) == ans


def test_UnionFind():
    for n, roads, ans in testcases:
        assert UnionFind().minScore(n, roads) == ans
