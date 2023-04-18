from Naive1768 import Solution as Naive

testcases = [
    ('abc', 'pqr', 'apbqcr'),
    ('ab', 'pqrs', 'apbqrs'),
    ('abcd', 'pq', 'apbqcd'),
]


def test_Naive():
    for word1, word2, ans in testcases:
        assert Naive().mergeAlternately(word1, word2) == ans
