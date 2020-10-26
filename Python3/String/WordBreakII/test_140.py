from Naive140 import Solution as naive
from Backtracking140 import Solution as backtracking
from DP140 import Solution as topdowndp

testcase = [
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"], [
        "cats and dog",
        "cat sand dog"
    ]),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"], [
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"
    ]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ("cat", ["cat"], ["cat"]),
    ("cat", [], []),
]


def test_naive():
    for s, wordDict, ans in testcase:
        assert sorted(naive().wordBreak(s, wordDict)) == sorted(ans)


def test_backtracking():
    for s, wordDict, ans in testcase:
        assert sorted(backtracking().wordBreak(s, wordDict)) == sorted(ans)


def test_topdowndp():
    for s, wordDict, ans in testcase:
        assert sorted(topdowndp().wordBreak(s, wordDict)) == sorted(ans)
