from Naive1232 import Solution as naive

testcase = [
    ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
    ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
    ([[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]], False),
    ([[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]], True),
    ([[1, 2], [1, 3]], True),
    ([[1, 2]], False)
]


def test_naive():
    for coordinates, ans in testcase:
        assert naive().checkStraightLine(coordinates) == ans
