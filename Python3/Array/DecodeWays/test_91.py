from Naive91 import Solution as naive

testcase = [
    ('12', 2),
    ('226', 3),
    ('0', 0),
    ('10', 1),
    ('01', 0),
    ('301', 0),
    ('27', 1),
    ('101', 1),
    ('12120', 3),
]


def test_naive():
    for s, ans in testcase:
        assert naive().numDecodings(s) == ans
