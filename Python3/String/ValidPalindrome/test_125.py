from Naive125 import Solution as naive
from Naive2_125 import Solution as two_pointer

testcase = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    (" ", True),
    ("0P", False)
]


def test_naive():
    for s, ans in testcase:
        assert naive().isPalindrome(s) == ans


def test_two_pointer():
    for s, ans in testcase:
        assert two_pointer().isPalindrome(s) == ans
