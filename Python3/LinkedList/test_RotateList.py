from LinkedList.RotateList.Naive061 import Solution as naive
from LinkedList.ListNodeModule import compareListNode, listNodeConverter

testcase = [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([0, 1, 2], 4, [2, 0, 1]),
    ([1], 0, [1])
]


def test_naive():
    for lst, k, ans in testcase:
        assert compareListNode(naive().rotateRight(
            listNodeConverter(lst), k), listNodeConverter(ans))
