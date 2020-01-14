from Recursive139 import Solution as recursive_with_memory

testcase = [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)
]


def test_recursive():
    for s, wordDict, ans in testcase:
        assert recursive_with_memory().wordBreak(s, wordDict) == ans
