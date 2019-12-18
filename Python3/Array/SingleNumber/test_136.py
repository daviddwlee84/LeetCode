from HT136 import Solution as HT

testcase = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([3], 3)
]


def test_HT():
    for nums, ans in testcase:
        assert HT().singleNumber(nums) == ans
