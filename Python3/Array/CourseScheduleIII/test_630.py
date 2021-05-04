from PriorityQueue630 import Solution as PQ
from TopDownDP630 import Solution as TDDP

testcases = [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
    ([[1, 2]], 1),
    ([[3, 2], [4, 3]], 0),
    ([[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]], 4),
]


def test_TDDP():
    for courses, ans in testcases:
        assert TDDP().scheduleCourse(courses) == ans


def test_PQ():
    for courses, ans in testcases:
        assert PQ().scheduleCourse(courses) == ans
