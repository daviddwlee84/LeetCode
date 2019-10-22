from BruteForce1143 import Solution as BruteForce
from DP1143 import Solution as DP

testcases = [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
    ("abc", "", 0),
    ("", "", 0),
    ("oxcpqrsvwf", "shmtulqrypy", 2),
    ("papmretkborsrurgtina", "nsnupotstmnkfcfavaxgl", 6)
]

def test_bruteForce():
    for text1, text2, ans in testcases:
        assert BruteForce().longestCommonSubsequence(text1, text2) == ans

def test_DP():
    for text1, text2, ans in testcases:
        assert DP().longestCommonSubsequence(text1, text2) == ans
