from BFS1971 import Solution as BFS
from DFS1971 import Solution as DFS
from UnionFind1971 import Solution as UnionFind


testcases = [
    (3, [[0,1],[1,2],[2,0]], 0, 2, True),
    (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False),
    (1, [], 0, 0, True),
]

def test_BFS():
    for n, edges, source, destination, ans in testcases:
        assert BFS().validPath(n, edges, source, destination) == ans

def test_DFS():
    for n, edges, source, destination, ans in testcases:
        assert DFS().validPath(n, edges, source, destination) == ans

def test_UnionFind():
    for n, edges, source, destination, ans in testcases:
        assert UnionFind().validPath(n, edges, source, destination) == ans
