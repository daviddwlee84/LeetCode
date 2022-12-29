from Naive392 import Solution as naive

testcase = [
    ("b", "c", False),
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("aaaaaa", "bbaaaa", False),
]


def test_naive():
    for s, t, ans in testcase:
        assert naive().isSubsequence(s, t) == ans
