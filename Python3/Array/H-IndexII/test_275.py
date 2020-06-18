from Linear275 import Solution as linear
from BinarySearch275 import Solution as binarysearch

testcase = [
    ([0, 1, 3, 5, 6], 3),
    ([], 0),
    ([0], 0),
    ([1], 1),
    ([1, 1], 1),
    ([1, 2], 1),
]


def test_linear():
    for citations, ans in testcase:
        assert linear().hIndex(citations) == ans


def test_binarysearch():
    for citations, ans in testcase:
        assert binarysearch().hIndex(citations) == ans
