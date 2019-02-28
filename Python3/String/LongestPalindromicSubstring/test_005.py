from Naive005 import Solution as Naive
from DP005 import Solution as DP

strings = []
strings.append("babad")
strings.append("cbbd")
strings.append("ac")
strings.append("bb")
strings.append("ccc")

answer = []
answer.append(["bab", "aba"])
answer.append(["bb"])
answer.append(["a", "c"])
answer.append(["bb"])
answer.append(["ccc"])

def test_naive():
    for i, s in enumerate(strings):
        assert any([Naive().longestPalindrome(s) == a for a in answer[i]])
