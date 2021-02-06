from Stack071 import Solution as stack
from Naive071 import Solution as naive

testcase = [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
    ("/a/../../b/../c//.//", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c")
]


def test_stack():
    for path, ans in testcase:
        assert stack().simplifyPath(path) == ans


def test_naive():
    for path, ans in testcase:
        assert naive().simplifyPath(path) == ans
