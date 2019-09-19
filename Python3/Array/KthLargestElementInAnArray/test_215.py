from QuickSort215 import Solution as quickSort
from SelectionSortLike215 import Solution as selectionSort

numbers = [
    [3, 2, 1, 5, 6, 4],
    [3, 2, 3, 1, 2, 4, 5, 5, 6]
]

ks = [
    2,
    4
]

answer = [
    5,
    4
]


def test_quickSort():
    for nums, k, ans in zip(numbers, ks, answer):
        assert quickSort().findKthLargest(nums, k) == ans

def test_selectionSort():
    for nums, k, ans in zip(numbers, ks, answer):
        assert selectionSort().findKthLargest(nums, k) == ans
