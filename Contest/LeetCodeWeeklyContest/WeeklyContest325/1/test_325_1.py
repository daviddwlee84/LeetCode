from Naive import Solution as Naive

testcases = [
    (["hello", "i", "am", "leetcode", "hello"], "hello", 1, 1),
    (["a", "b", "leetcode"], "leetcode", 0, 1),
    (["i", "eat", "leetcode"], "ate", 0, -1),
    (["odjrjznxpn", "cyulttuabe", "zqxkdoeszk", "yeewpgriok", "odjrjznxpn", "btqpvxpjzv",
     "ukyudladhk", "ukyudladhk", "odjrjznxpn", "yeewpgriok"], "odjrjznxpn", 5, 1),
]


def test_naive():
    for words, target, startIndex, ans in testcases:
        assert Naive().closetTarget(words, target, startIndex) == ans
