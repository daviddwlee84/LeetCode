from Greedy2279 import Solution as Greedy

testcases = [
    ([2, 3, 4, 5], [1, 2, 4, 4], 2, 3),
    ([10, 2, 2], [2, 2, 0], 100, 3),
]


def test_Greedy():
    for capacity, rocks, additionalRocks, ans in testcases:
        assert Greedy().maximumBags(capacity, rocks, additionalRocks) == ans
