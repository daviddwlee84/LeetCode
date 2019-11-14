from Naive128 import Solution as naive

testcase = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0], 1),
    ([], 0)
]

def test_naive():
    for nums, ans in testcase:
        assert naive().longestConsecutive(nums) == ans
