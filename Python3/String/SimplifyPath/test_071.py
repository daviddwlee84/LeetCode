from Stack071 import Solution as stack
from Naive071 import Solution as naive
from Stack2_071 import Solution as stack2

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


def test_stack2():
    for path, ans in testcase:
        assert stack2().simplifyPath(path) == ans
