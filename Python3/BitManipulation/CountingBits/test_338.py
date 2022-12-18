from Naive338 import Solution as Naive

testcases = [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
]


def test_naive():
    for n, ans in testcases:
        assert Naive().countBits(n) == ans
