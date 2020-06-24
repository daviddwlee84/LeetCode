from Naive096 import Solution as naive

testcase = [
    (3, 5),
    (0, 0),
    (1, 1),
    (2, 2)
]


def test_naive():
    for n, ans in testcase:
        assert naive().numTrees(n) == ans
