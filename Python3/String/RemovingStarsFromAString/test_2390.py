from Stack2390 import Solution as Stack

testcases = [
    ('leet**cod*e', 'lecoe'),
    ('erase*****', ''),
]


def test_Stack():
    for s, ans in testcases:
        assert Stack().removeStars(s) == ans
