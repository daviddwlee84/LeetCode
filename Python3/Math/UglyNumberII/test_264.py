from PriorityQueue264 import Solution as pq
from DP264 import Solution as dp

testcase = [
    (11, 15),
    (10, 12),
    (9, 10),
    (8, 9),
    (7, 8),
    (6, 6),
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1)
]


def test_pq():
    for n, ans in testcase:
        assert pq().nthUglyNumber(n) == ans


def test_dp():
    for n, ans in testcase:
        assert dp().nthUglyNumber(n) == ans
