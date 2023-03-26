from DFSWithTime2360 import Solution as DFSWithTime

testcases = [
    ([3, 3, 4, 2, 3], 3),
    ([2, -1, 3, 1], -1),
    ([1, 2, 0, 4, 5, 6, 3, 8, 9, 7], 4),
]


def test_DFSWithTime():
    for edges, ans in testcases:
        assert DFSWithTime().longestCycle(edges) == ans
