from Stack071 import Solution as stack

testcase = [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
    ("/a/../../b/../c//.//", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c")
]

def test_backtrack():
    for path, ans in testcase:
        assert stack().simplifyPath(path) == ans
