from Naive621 import Solution as naive
testcase = [
    (["A", "A", "A", "B", "B", "B"], 2, 8),
    (["A", "A", "A", "B", "B", "B"], 0, 6),
    (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    (["A", "A", "A", "B", "B", "B"], 3, 10),
]


def test_naive():
    for tasks, n, ans in testcase:
        assert naive().leastInterval(tasks, n) == ans
