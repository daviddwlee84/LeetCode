from Heap1046 import Solution as Heap
from InsertionSort1046 import Solution as InsertionSort

testcase = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([1], 1),
    ([], 0),
    ([2, 2], 0)
]


def test_Heap():
    for stones, ans in testcase:
        assert Heap().lastStoneWeight(stones) == ans


def test_InsertionSort():
    for stones, ans in testcase:
        assert InsertionSort().lastStoneWeight(stones) == ans
