from TopDownDP516 import Solution as TopDownDP

testcases = [
    ('bbbab', 4),
    ('cbbd', 2),
]


def test_TopDownDP():
    for s, ans in testcases:
        assert TopDownDP().longestPalindromeSubseq(s) == ans
