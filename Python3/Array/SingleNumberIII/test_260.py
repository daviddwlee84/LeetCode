from BitManipulation260 import Solution as bm

testcase = [
    ([1, 2, 1, 3, 2, 5], [3, 5])
]


def test_bm():
    for nums, ans in testcase:
        assert sorted(bm().singleNumber(nums)) == sorted(ans)
