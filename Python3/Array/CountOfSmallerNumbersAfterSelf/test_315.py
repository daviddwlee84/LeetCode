from BinaryIndexedTree315 import Solution as FenwickTree

testcases = [
    ([5, 2, 6, 1], [2, 1, 1, 0]),
    ([-1], [0]),
    ([-1, -1], [0, 0]),
    ([2, 0, 1], [2, 0, 0]),
    ([2, 1, 1], [2, 0, 0]),
]


def test_FenwickTree():
    for nums, ans in testcases:
        assert list(FenwickTree().countSmaller(nums)) == ans, f'Failed at Case: {nums}'
