from Naive797 import Solution as naive
from Backtracking797 import Solution as backtracking

testcase = [
    ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
    ([[]], [[0]]),
    ([[1], []], [[0, 1]])
]


def test_naive():
    for graph, ans in testcase:
        assert sorted(naive().allPathsSourceTarget(graph)) == sorted(ans)


def test_backtracking():
    for graph, ans in testcase:
        assert sorted(backtracking().allPathsSourceTarget(
            graph)) == sorted(ans)
