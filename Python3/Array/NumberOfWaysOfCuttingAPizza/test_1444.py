from PrefixSumDP1444 import Solution as PrefixSumDP

testcases = [
    (["A..", "AAA", "..."], 3, 3),
    (["A..", "AA.", "..."], 3, 1),
    (["A..", "A..", "..."], 1, 1),
]


def test_PrefixSumDP():
    for pizza, k, ans in testcases:
        assert PrefixSumDP().ways(pizza, k) == ans
