from LinkedList.ListNodeModule import listNodeConverter as lc
from LinkedList.ListNodeModule import compareListNode as cp
from LinkedList.RemoveLinkedListElements.Naive203 import Solution as naive
from LinkedList.RemoveLinkedListElements.SinglePointer203 import Solution as singlepointer

testcase = [
    ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
    ([6, 1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1], 2, [1, 1]),
    ([], 1, []),
    ([1], 1, [])
]


def test_naive():
    for head, val, ans in testcase:
        assert cp(naive().removeElements(lc(head), val), lc(ans))


def test_singlepointer():
    for head, val, ans in testcase:
        assert cp(singlepointer().removeElements(lc(head), val), lc(ans))
