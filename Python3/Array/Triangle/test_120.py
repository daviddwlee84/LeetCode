from Naive120 import Solution as naive

testcase = [
    (
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ],
        11
    ),
    (
        [
            [2],
        ],
        2
    ),
]


def test_naive():
    for triangle, ans in testcase:
        assert naive().minimumTotal(triangle) == ans
