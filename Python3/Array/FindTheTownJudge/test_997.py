from Naive997 import Solution as naive

testcase = [
    (2, [[1, 2]], 2),
    (3, [[1, 3], [2, 3]], 3),
    (3, [[1, 3], [2, 3], [3, 1]], -1),
    (3, [[1, 2], [2, 3]], -1),
    (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
    (1, [], 1),
]


def test_naive():
    for N, trust, ans in testcase:
        assert naive().findJudge(N, trust) == ans
