from TopDownDP1312 import Solution as TopDownDP

testcases = [
    ('zzazz', 0),
    ('mbadm', 2),
    ('leetcode', 5),
]


def test_TopDownDP():
    for s, ans in testcases:
        assert TopDownDP().minInsertions(s) == ans
