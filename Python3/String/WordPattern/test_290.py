from HashMap290 import Solution as HashMap

testcases = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abba", "dog dog dog dog", False),
    ("aaa", "aa aa aa aa", False),
]


def test_hashmap():
    for pattern, s, ans in testcases:
        assert HashMap().wordPattern(pattern, s) == ans
