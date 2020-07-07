from Naive263 import Solution as naive

testcase = [
    (6, True),
    (8, True),
    (14, False),
    (-2, False),
    (0, False)
]


def test_naive():
    for num, ans in testcase:
        assert naive().isUgly(num) == ans
