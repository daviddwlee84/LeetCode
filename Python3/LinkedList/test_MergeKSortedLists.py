from LinkedList.MergeKSortedLists.Naive023 import Solution as naive
from LinkedList.MergeKSortedLists.DC023 import Solution as dc
from LinkedList.ListNodeModule import listNodeConverter, compareListNode

listsA1 = [[2],[],[-1]]
listsB1 = [[1,4,5],[1,3,4],[2,6]]

answer1 = listNodeConverter([-1,2])
answer2 = listNodeConverter([1,1,2,3,4,4,5,6])

def test_naive():
    assert compareListNode(naive().mergeKLists([listNodeConverter(lst) for lst in listsA1]), answer1)
    assert compareListNode(naive().mergeKLists([listNodeConverter(lst) for lst in listsB1]), answer2)

listsA2 = [[2],[],[-1]]
listsB2 = [[1,4,5],[1,3,4],[2,6]]

def test_dc():
    assert compareListNode(dc().mergeKLists([listNodeConverter(lst) for lst in listsA2]), answer1)
    assert compareListNode(dc().mergeKLists([listNodeConverter(lst) for lst in listsB2]), answer2)

    