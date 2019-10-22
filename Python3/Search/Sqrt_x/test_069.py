from Naive069 import Solution as Naive
from BinarySearch069 import Solution as BinarySearch

testcase = [
    (4, 2),
    (8, 2),
    (0, 0),
    (1, 1),
    (2, 1)
]

def test_naive():
    for x, ans in testcase:
        assert Naive().mySqrt(x) == ans

def test_binary_search():
    for x, ans in testcase:
        assert BinarySearch().mySqrt(x) == ans
