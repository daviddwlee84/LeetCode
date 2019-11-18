from Naive088 import Solution as naive

testcase = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([], 0, [], 0, []),
    ([0], 0, [87], 1, [87]),
    ([87], 1, [], 0, [87])
]


def test_naive():
    for nums1, m, nums2, n, ans in testcase:
        naive().merge(nums1, m, nums2, n)  # in-place
        assert nums1 == ans
