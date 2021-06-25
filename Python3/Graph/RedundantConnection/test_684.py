from DSU684 import Solution as DSU
from CyclePreventionDFS684 import Solution as DFS
from UnionFind684 import Solution as DSU2

testcases = [
    ([[1, 2], [1, 3], [2, 3]], [2, 3]),
    ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4])
]


def test_DSU():
    for edges, ans in testcases:
        assert tuple(DSU().findRedundantConnection(edges)) == tuple(ans)


def test_DFS():
    for edges, ans in testcases:
        assert tuple(DFS().findRedundantConnection(edges)) == tuple(ans)


def test_DSU2():
    for edges, ans in testcases:
        assert tuple(DSU2().findRedundantConnection(edges)) == tuple(ans)
