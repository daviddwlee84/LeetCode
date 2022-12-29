from Greedy1834 import Solution as Greedy
from Heap1834 import Solution as Heap
from HeapImprove1834 import Solution as HeapImprove

testcases = [
    ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
    ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
    # ([[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [
    #  33, 6], [45, 4], [18, 18], [46, 39], [12, 24]], [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7])
]


def test_Greedy():
    for tasks, ans in testcases:
        assert Greedy().getOrder(tasks.copy()) == ans


def test_Heap():
    for tasks, ans in testcases:
        assert Heap().getOrder(tasks.copy()) == ans


def test_HeapImprove():
    for tasks, ans in testcases:
        assert HeapImprove().getOrder(tasks.copy()) == ans
