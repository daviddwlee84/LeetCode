from Naive1539 import Solution as Naive
from Naive2_1539 import Solution as Naive2
from BinarySearch1539 import Solution as BinarySearch
from Bisect1539 import Solution as Bisect

testcases = [
    ([2, 3, 4, 7, 11], 5, 9),
    ([1, 2, 3, 4], 2, 6),
    ([1, 2], 1, 3),
]


def test_Naive():
    for arr, k, ans in testcases:
        assert Naive().findKthPositive(arr, k) == ans


def test_Naive2():
    for arr, k, ans in testcases:
        assert Naive2().findKthPositive(arr, k) == ans


def test_BinarySearch():
    for arr, k, ans in testcases:
        assert BinarySearch().findKthPositive(arr, k) == ans


# This require Python 3.10
# def test_Bisect():
#     for arr, k, ans in testcases:
#         assert Bisect().findKthPositive(arr, k) == ans
