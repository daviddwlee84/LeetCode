from LinkedList.ListNodeModule import listNodeConverter, compareListNode, printListNode

from LinkedList.RemoveDuplicatesFromSortedList.Naive083 import Solution as Naive

testcases = [
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3]),
    ([1, 2, 3, 3, 3], [1, 2, 3]),
    ([1, 1, 1], [1])
]

def test_naive():
    for raw_case, raw_ans in testcases:
        case = listNodeConverter(raw_case)
        ans = listNodeConverter(raw_ans)
        # printListNode(case)
        # printListNode(Naive().deleteDuplicates(case))
        assert compareListNode(ans, Naive().deleteDuplicates(case)) == True
