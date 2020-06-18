from CumulativeSum274 import Solution as cumulativesum

testcase = [
    ([3, 0, 6, 1, 5], 3),
    ([0, 1, 3, 5, 6], 3),
    ([], 0),
    ([0], 0),
    ([1], 1),
    ([1, 1], 1),
    ([1, 2], 1),
]


def test_cumulativesum():
    for citations, ans in testcase:
        assert cumulativesum().hIndex(citations) == ans
