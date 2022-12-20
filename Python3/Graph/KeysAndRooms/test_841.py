from DFS841 import Solution as DFS
from DFS_loop841 import Solution as DFS_loop

testcases = [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False),
]


def test_dfs():
    for rooms, ans in testcases:
        assert DFS().canVisitAllRooms(rooms) == ans


def test_dfs_loop():
    for rooms, ans in testcases:
        assert DFS_loop().canVisitAllRooms(rooms) == ans
