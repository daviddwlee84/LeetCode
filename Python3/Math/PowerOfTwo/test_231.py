from Naive231 import Solution as naive
from String231 import Solution as string

testcase = [
    (0, False),
    (1, True),
    (2, True),
    (16, True),
    (218, False),
    (-16, False)
]


def test_naive():
    for n, ans in testcase:
        assert naive().isPowerOfTwo(n) == ans


def test_string():
    for n, ans in testcase:
        assert string().isPowerOfTwo(n) == ans
