from Pythonic151 import Solution as Pythonic
from Trick151 import Solution as Trick
from Naive151 import Solution as Naive
from CStyle151 import Solution as CStyle

testcases = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world!  ", "world! hello"),
    ("a good    example", "example good a")
]


def test_pythonic():
    for s, ans in testcases:
        assert Pythonic().reverseWords(s) == ans


def test_trick():
    for s, ans in testcases:
        assert Trick().reverseWords(s) == ans


def test_naive():
    for s, ans in testcases:
        assert Naive().reverseWords(s) == ans


def test_CStyle():
    for s, ans in testcases:
        assert CStyle().reverseWords(s) == ans
