from ProductList138 import Solution as PL
from ProductList2_138 import Solution as PL2
from SingleProductList138 import Solution as SPL

testcase = [
    ([4, 5, 1, 8, 2],
     [80, 64, 320, 40, 160]),
    ([1, 2, 3, 4],
     [24, 12, 8, 6])
]


def test_pl():
    for nums, ans in testcase:
        assert PL().productExceptSelf(nums) == ans


def test_pl2():
    for nums, ans in testcase:
        assert PL2().productExceptSelf(nums) == ans


def test_spl():
    for nums, ans in testcase:
        assert SPL().productExceptSelf(nums) == ans
