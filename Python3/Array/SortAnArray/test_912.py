from QuickSort912 import Solution as QuickSort
from HeapSort912 import Solution as HeapSort

testcases = [
    [5, 2, 3, 1],
    [5, 1, 1, 2, 0, 0],
    [1, 2, 3, 4],
    [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4],
]


# The worst case will TLE
def test_QuickSort():
    for nums in testcases:
        assert QuickSort().sortArray(nums.copy()) == sorted(nums)

def test_HeapSort():
    for nums in testcases:
        assert HeapSort().sortArray(nums.copy()) == sorted(nums)
