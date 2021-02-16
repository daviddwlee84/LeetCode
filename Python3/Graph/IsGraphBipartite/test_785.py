from Color785 import Solution as Color


testcases = [
    ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
    ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
]


def test_color():
    for case, ans in testcases:
        assert Color().isBipartite(case) == ans
