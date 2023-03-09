from DP2_072 import Solution as DP2
from DP072 import Solution as DP
from Recursive072 import Solution as Recursive
from RecursiveWithMemory072 import Solution as RecursiveWithMemory

testcase = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "", 0),
    ("a", "a", 0),
    ("a", "", 1),  # add
    ("ab", "a", 1),  # delete
    ("a", "e", 1)  # replace
]


def test_dp():
    for word1, word2, ans in testcase:
        assert DP().minDistance(word1, word2) == ans


def test_recursive():
    for word1, word2, ans in testcase:
        assert Recursive().minDistance(word1, word2) == ans


def test_recursive_withMemory():
    for word1, word2, ans in testcase:
        assert RecursiveWithMemory().minDistance(word1, word2) == ans


def test_dp2():
    for word1, word2, ans in testcase:
        assert DP2().minDistance(word1, word2) == ans
