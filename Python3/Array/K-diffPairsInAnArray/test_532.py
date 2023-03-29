from Naive532 import Solution as naive
from HT532 import Solution as hashtable
from Naive2_532 import Solution as naive2

testcases = [
    ([3, 1, 4, 1, 5], 2, 2),
    ([1, 2, 3, 4, 5], 1, 4),
    ([1, 3, 1, 5, 4], 0, 1),
    ([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3, 2)
]


def test_naive():
    for nums, k, ans in testcases:
        assert naive().findPairs(nums, k) == ans


def test_hashtable():
    for nums, k, ans in testcases:
        assert hashtable().findPairs(nums, k) == ans


# def test_naive2():
#     for nums, k, ans in testcases:
#         assert naive2().findPairs(nums, k) == ans
