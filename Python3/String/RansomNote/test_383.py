from Naive383 import Solution as Naive
from Better383 import Solution as Better

testcases = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
]


def test_Naive():
    for ransomNote, magazine, ans in testcases:
        assert Naive().canConstruct(ransomNote, magazine) == ans


def test_Better():
    for ransomNote, magazine, ans in testcases:
        assert Better().canConstruct(ransomNote, magazine) == ans
