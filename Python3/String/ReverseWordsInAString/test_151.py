from Pythonic151 import Solution as Pythonic
from Trick151 import Solution as Trick

testcases = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world!  ", "world! hello"),
    ("a good    example", "example good a")
]

def test_pythonic():
    for s, ans in testcases:
        assert Pythonic().reverseWords(s) == ans

def test_trick():
    for s, ans in testcases:
        assert Trick().reverseWords(s) == ans
