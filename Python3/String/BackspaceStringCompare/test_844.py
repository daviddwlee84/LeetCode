from Naive844 import Solution as naive
from TwoPointer844 import Solution as twoPointer

testcase = [
    ("ab#c", "ab#c", True),
    ("ab##", "c#d#", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False),
    ("y#fo##f", "y#f#o##f", True)
]


def test_naive():
    for S, T, ans in testcase:
        assert naive().backspaceCompare(S, T) == ans


def test_twoPointer():
    for S, T, ans in testcase:
        assert twoPointer().backspaceCompare(S, T) == ans
