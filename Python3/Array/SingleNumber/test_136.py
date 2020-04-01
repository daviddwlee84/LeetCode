from HT136 import Solution as HT
from Set136 import Solution as Set
from BM136 import Solution as BM

testcase = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([3], 3)
]


def test_HT():
    for nums, ans in testcase:
        assert HT().singleNumber(nums) == ans


def test_Set():
    for nums, ans in testcase:
        assert Set().singleNumber(nums) == ans


def test_BM():
    for nums, ans in testcase:
        assert BM().singleNumber(nums) == ans
