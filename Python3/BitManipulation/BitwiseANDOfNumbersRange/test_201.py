from Naive201 import Solution as naive
from Improve201 import Solution as improve

testcase = [
    (5, 7, 4),
    (0, 1, 0),
    (0, 2147483647, 0),
    (1, 2147483647, 0)
]


# this takes too long
# def test_naive():
#     for m, n, ans in testcase:
#         assert naive().rangeBitwiseAnd(m, n) == ans


def test_improve():
    for m, n, ans in testcase:
        assert improve().rangeBitwiseAnd(m, n) == ans
