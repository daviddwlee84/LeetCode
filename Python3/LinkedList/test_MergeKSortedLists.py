from LinkedList.MergeKSortedLists.Naive023 import Solution as naive
from LinkedList.ListNodeModule import listNodeConverter, compareListNode

lists1 = [[2],[],[-1]]
lists2 = [[1,4,5],[1,3,4],[2,6]]

answer1 = listNodeConverter([-1,2])
answer2 = listNodeConverter([1,1,2,3,4,4,5,6])

def test_naive():
    assert compareListNode(naive().mergeKLists([listNodeConverter(lst) for lst in lists1]), answer1)
    assert compareListNode(naive().mergeKLists([listNodeConverter(lst) for lst in lists2]), answer2)
    