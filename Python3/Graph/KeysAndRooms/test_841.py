from DFS841 import Solution as DFS

testcases = [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False),
]


def test_dfs():
    for rooms, ans in testcases:
        assert DFS().canVisitAllRooms(rooms) == ans
