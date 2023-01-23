from Naive997 import Solution as naive
from Improve997 import Solution as improve
from Naive2_997 import Solution as naive2

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


def test_improve():
    for N, trust, ans in testcase:
        assert improve().findJudge(N, trust) == ans


def test_naive2():
    for N, trust, ans in testcase:
        assert naive2().findJudge(N, trust) == ans
