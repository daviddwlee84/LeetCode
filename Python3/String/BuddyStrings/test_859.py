from Naive859 import Solution as naive
from Naive2_859 import Solution as naive2

testcase = [
    ('ab', 'ba', True),
    ('ab', 'ab', False),
    ('aa', 'aa', True),
    ('aaaaaaabc', 'aaaaaaacb', True),
    ('', 'aa', False),
]


def test_naive():
    for A, B, ans in testcase:
        assert naive().buddyStrings(A, B) == ans

def test_naive2():
    for A, B, ans in testcase:
        assert naive2().buddyStrings(A, B) == ans
