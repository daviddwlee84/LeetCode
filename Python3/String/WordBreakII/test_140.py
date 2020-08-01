from Naive140 import Solution as naive

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
