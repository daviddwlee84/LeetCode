from DFS1319 import Solution as DFS

testcases = [
    (4, [[0, 1], [0, 2], [1, 2]], 1),
    (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2),
    (6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1),
]


def test_DFS():
    for n, connections, ans in testcases:
        assert DFS().makeConnected(n, connections) == ans
