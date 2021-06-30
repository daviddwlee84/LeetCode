from Naive1004 import Solution as naive

testcases = [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ([0, 0, 1, 1, 1, 0, 0, 1, 1], 0, 3),
]


def test_naive():
    for nums, k, ans in testcases:
        assert naive().longestOnes(nums, k) == ans
