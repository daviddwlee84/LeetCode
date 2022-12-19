from Naive1071 import Solution as Naive


testcases = [
    ('ABCABC', 'ABC', 'ABC'),
    ('ABABAB', 'ABAB', 'AB'),
    ('LEET', 'CODE', ''),
    ('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXX'),
]


def test_naive():
    for str1, str2, ans in testcases:
        assert Naive().gcdOfStrings(str1, str2) == ans
