from LinkedList.MergeKSortedLists.Naive023 import Solution as naive
from LinkedList.MergeKSortedLists.DC023 import Solution as dc
from LinkedList.MergeKSortedLists.Naive2_023 import Solution as naive2
from LinkedList.MergeKSortedLists.DC2_023 import Solution as dc2
from LinkedList.MergeKSortedLists.Heap023 import Solution as heap
from LinkedList.ListNodeModule import listNodeConverter, compareListNode

listsA1 = [[2], [], [-1]]
listsB1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
listsC1 = [[1, 3], [-8], [-9, -7, -3, -2, -2, -1, 2],
           [], [-7, -7, -7, -2, -1, -1, 4]]

answer1 = listNodeConverter([-1, 2])
answer2 = listNodeConverter([1, 1, 2, 3, 4, 4, 5, 6])
answer3 = listNodeConverter(
    [-9, -8, -7, -7, -7, -7, -3, -2, -2, -2, -1, -1, -1, 1, 2, 3, 4])


def test_naive():
    assert compareListNode(naive().mergeKLists(
        [listNodeConverter(lst) for lst in listsA1]), answer1)
    assert compareListNode(naive().mergeKLists(
        [listNodeConverter(lst) for lst in listsB1]), answer2)
    assert compareListNode(naive().mergeKLists(
        [listNodeConverter(lst) for lst in listsC1]), answer3)


listsA2 = [[2], [], [-1]]
listsB2 = [[1, 4, 5], [1, 3, 4], [2, 6]]
listsC2 = [[1, 3], [-8], [-9, -7, -3, -2, -2, -1, 2],
           [], [-7, -7, -7, -2, -1, -1, 4]]


def test_dc():
    assert compareListNode(dc().mergeKLists(
        [listNodeConverter(lst) for lst in listsA2]), answer1)
    assert compareListNode(dc().mergeKLists(
        [listNodeConverter(lst) for lst in listsB2]), answer2)
    assert compareListNode(dc().mergeKLists(
        [listNodeConverter(lst) for lst in listsC2]), answer3)


listsA3 = [[2], [], [-1]]
listsB3 = [[1, 4, 5], [1, 3, 4], [2, 6]]
listsC3 = [[1, 3], [-8], [-9, -7, -3, -2, -2, -1, 2],
           [], [-7, -7, -7, -2, -1, -1, 4]]


def test_naive2():
    assert compareListNode(naive2().mergeKLists(
        [listNodeConverter(lst) for lst in listsA3]), answer1)
    assert compareListNode(naive2().mergeKLists(
        [listNodeConverter(lst) for lst in listsB3]), answer2)
    assert compareListNode(naive2().mergeKLists(
        [listNodeConverter(lst) for lst in listsC3]), answer3)


listsA4 = [[2], [], [-1]]
listsB4 = [[1, 4, 5], [1, 3, 4], [2, 6]]
listsC4 = [[1, 3], [-8], [-9, -7, -3, -2, -2, -1, 2],
           [], [-7, -7, -7, -2, -1, -1, 4]]


def test_dc2():
    assert compareListNode(dc2().mergeKLists(
        [listNodeConverter(lst) for lst in listsA4]), answer1)
    assert compareListNode(dc2().mergeKLists(
        [listNodeConverter(lst) for lst in listsB4]), answer2)
    assert compareListNode(dc2().mergeKLists(
        [listNodeConverter(lst) for lst in listsC4]), answer3)


listsA5 = [[2], [], [-1]]
listsB5 = [[1, 4, 5], [1, 3, 4], [2, 6]]
listsC5 = [[1, 3], [-8], [-9, -7, -3, -2, -2, -1, 2],
           [], [-7, -7, -7, -2, -1, -1, 4]]


def test_heap():
    assert compareListNode(heap().mergeKLists(
        [listNodeConverter(lst) for lst in listsA5]), answer1)
    assert compareListNode(heap().mergeKLists(
        [listNodeConverter(lst) for lst in listsB5]), answer2)
    assert compareListNode(heap().mergeKLists(
        [listNodeConverter(lst) for lst in listsC5]), answer3)
