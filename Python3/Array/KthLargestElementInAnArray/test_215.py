from QuickSort215 import Solution as quickSort
from SelectionSortLike215 import Solution as selectionSort
from Naive215 import Solution as naive
from HeapCheat215 import Solution as heapCheat
from Heap215 import Solution as heap
from QuickSelect215 import Solution as quickSelect
from QuickSelect2_215 import Solution as quickSelect2

numbers = [
    [3, 2, 1, 5, 6, 4],
    [3, 2, 3, 1, 2, 4, 5, 5, 6],
    [5, 2, 4, 1, 3, 6, 0]
]

ks = [
    2,
    4,
    4
]

answer = [
    5,
    4,
    3
]


def test_quickSort():
    for nums, k, ans in zip(numbers, ks, answer):
        assert quickSort().findKthLargest(nums.copy(), k) == ans


def test_selectionSort():
    for nums, k, ans in zip(numbers, ks, answer):
        assert selectionSort().findKthLargest(nums.copy(), k) == ans


def test_naive():
    for nums, k, ans in zip(numbers, ks, answer):
        assert naive().findKthLargest(nums.copy(), k) == ans


def test_heapCheat():
    for nums, k, ans in zip(numbers, ks, answer):
        assert heapCheat().findKthLargest(nums.copy(), k) == ans


def test_heap():
    for nums, k, ans in zip(numbers, ks, answer):
        assert heap().findKthLargest(nums.copy(), k) == ans


def test_quickSelect():
    for nums, k, ans in zip(numbers, ks, answer):
        assert quickSelect().findKthLargest(nums.copy(), k) == ans


def test_quickSelect2():
    for nums, k, ans in zip(numbers, ks, answer):
        assert quickSelect2().findKthLargest(nums.copy(), k) == ans
