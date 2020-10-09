from Sorting056 import Solution as sorting
from Naive056 import Solution as naive
from Better056 import Solution as better
from Graph056 import Solution as graph
from Tree056 import Solution as tree

testcase = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),
]


def test_sorting():
    for intervals, answer in testcase:
        assert sorting().merge(intervals.copy()) == answer


def test_naive():
    for intervals, answer in testcase:
        assert naive().merge(intervals.copy()) == answer


def test_better():
    for intervals, answer in testcase:
        assert better().merge(intervals.copy()) == answer


def test_graph():
    for intervals, answer in testcase:
        assert graph().merge(intervals.copy()) == answer


def test_tree():
    for intervals, answer in testcase:
        assert tree().merge(intervals.copy()) == answer
