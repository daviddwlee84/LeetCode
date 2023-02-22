from BinarySearch1011 import Solution as BinarySearch
from BinarySearchImprove1011 import Solution as BinarySearchImprove

testcases = [
    ({'weights': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'days': 5}, 15),
    ({'weights': [3, 2, 2, 4, 1, 4], 'days': 3}, 6),
    ({'weights': [1, 2, 3, 1, 1], 'days': 4}, 3)
]


def test_BinarySearch():
    for testcase, ans in testcases:
        assert BinarySearch().shipWithinDays(**testcase) == ans


def test_BinarySearchImprove():
    for testcase, ans in testcases:
        assert BinarySearchImprove().shipWithinDays(**testcase) == ans
