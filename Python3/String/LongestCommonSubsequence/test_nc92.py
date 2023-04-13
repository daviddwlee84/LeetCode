from DP_ReturnSubsequence import Solution as DP

# https://www.nowcoder.com/practice/6d29638c85bb4ffd80c020fe244baf11?tpId=196&tqId=37131&ru=/exam/oj
testcases = [
    ("1A2C3D4B56", "B1D23A456A", "123456"),
    ("abc", "def", "-1"),
    ("abc", "abc", "abc"),
    ("ab", "", "-1"),
]


def test_DP():
    for s1, s2, ans in testcases:
        assert DP().LCS(s1, s2) == ans
