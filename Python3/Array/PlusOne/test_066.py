from Naive066 import Solution as naive

testcase = [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0])
]


def test_naive():
    for case, ans in testcase:
        assert naive().plusOne(case) == ans
