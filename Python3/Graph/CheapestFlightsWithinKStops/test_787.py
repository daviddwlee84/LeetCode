from Naive787 import Solution as naive
from BFS787 import Solution as bfs
from DP787 import Solution as dp
from Naive2_787 import Solution as naive2

testcase = [
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    (3, [[0, 1, 100]], 0, 2, 0, -1),
    (3, [[0, 1, 2], [1, 2, 1], [2, 0, 10]], 1, 2, 1, 1),
    (5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [
     0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1, -1),
]


def test_naive():
    for n, flights, src, dst, K, ans in testcase:
        assert naive().findCheapestPrice(n, flights, src, dst, K) == ans


def test_bfs():
    for n, flights, src, dst, K, ans in testcase:
        assert bfs().findCheapestPrice(n, flights, src, dst, K) == ans


def test_dp():
    for n, flights, src, dst, K, ans in testcase:
        assert dp().findCheapestPrice(n, flights, src, dst, K) == ans


def test_naive2():
    for n, flights, src, dst, K, ans in testcase:
        assert naive2().findCheapestPrice(n, flights, src, dst, K) == ans
