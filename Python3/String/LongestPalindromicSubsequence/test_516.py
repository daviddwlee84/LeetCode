from TopDownDP516 import Solution as TopDownDP
from BottomUpDP516 import Solution as BottomUpDP

testcases = [
    ('bbbab', 4),
    ('cbbd', 2),
]


def test_TopDownDP():
    for s, ans in testcases:
        assert TopDownDP().longestPalindromeSubseq(s) == ans


def test_BottomUpDP():
    for s, ans in testcases:
        assert BottomUpDP().longestPalindromeSubseq(s) == ans
