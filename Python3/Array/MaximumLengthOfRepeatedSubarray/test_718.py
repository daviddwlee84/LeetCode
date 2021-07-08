from DP718 import Solution as DP

testcases = [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),
    ([0, 1, 1, 1, 1], [1, 0, 1, 0, 1], 2),
]


def test_DP():
    for nums1, nums2, ans in testcases:
        assert DP().findLength(nums1, nums2) == ans
