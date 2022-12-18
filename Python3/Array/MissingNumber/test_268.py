from Naive268 import Solution as Naive

testcases = [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
]

def test_naive():
    for nums, ans in testcases:
        assert Naive().missingNumber(nums) == ans
