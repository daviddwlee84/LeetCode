from Naive005 import Solution as Naive
from DP005 import Solution as DP

strings = []
strings.append("babad")
strings.append("cbbd")
strings.append("ac")
strings.append("bb")
strings.append("ccc")
strings.append("abcba")

answer = []
answer.append(["bab", "aba"])
answer.append(["bb"])
answer.append(["a", "c"])
answer.append(["bb"])
answer.append(["ccc"])
answer.append(["abcba"])

def test_naive():
    for i, s in enumerate(strings):
        assert any([Naive().longestPalindrome(s) == a for a in answer[i]])

def test_DP():
    for i, s in enumerate(strings):
        assert any([DP().longestPalindrome(s) == a for a in answer[i]])
