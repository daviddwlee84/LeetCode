from Naive125 import Solution as naive

testcase = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    ("0P", False)
]


def test_naive():
    for s, ans in testcase:
        assert naive().isPalindrome(s) == ans
