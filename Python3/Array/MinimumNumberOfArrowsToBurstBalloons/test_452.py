from Naive452 import Solution as naive

testcase = [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[1, 2]], 1),
    ([[2, 3], [2, 3]], 1),
    ([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]], 2),
]


def test_naive():
    for points, ans in testcase:
        assert naive().findMinArrowShots(points) == ans
