from Naive1046 import Solution as naive

testcase = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([1], 1),
    ([], 0),
    ([2, 2], 0)
]


def test_naive():
    for stones, ans in testcase:
        assert naive().lastStoneWeight(stones) == ans
