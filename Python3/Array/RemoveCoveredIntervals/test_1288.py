from Naive1288 import Solution as naive


testcase = [
    ([[1, 4], [2, 3]], 1),
    ([[0, 10], [5, 12]], 2),
    ([[3, 10], [4, 10], [5, 11]], 2),
    ([[1, 2], [1, 4], [3, 4]], 1),
    ([[34335, 39239], [15875, 91969], [29673, 66453], [53548, 69161], [40618, 93111]], 2),
]


def test_naive():
    for intervals, ans in testcase:
        assert naive().removeCoveredIntervals(intervals) == ans
