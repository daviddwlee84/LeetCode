from LinkedList.ListNodeModule import listNodeConverter, compareListNode
from LinkedList.InsertionSortList.Naive147 import Solution as naive

testcase = [
    (listNodeConverter([4, 2, 1, 3]), listNodeConverter([1, 2, 3, 4])),
    (listNodeConverter([]), listNodeConverter([])),
    (listNodeConverter([1]), listNodeConverter([1]))
]


def test_naive():
    for head, ans in testcase:
        assert compareListNode(naive().insertionSortList(head), ans)
