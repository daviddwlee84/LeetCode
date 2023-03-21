from Math2348 import Solution as Math
from SimplifiedMath2348 import Solution as SimplifiedMath

testcases = [
    ([1, 3, 0, 0, 2, 0, 0, 4], 6),
    ([0, 0, 0, 2, 0, 0], 9),
    ([2, 10, 2019], 0),
]


def test_Math():
    for nums, ans in testcases:
        assert Math().zeroFilledSubarray(nums) == ans


def test_SimplifiedMath():
    for nums, ans in testcases:
        assert SimplifiedMath().zeroFilledSubarray(nums) == ans
