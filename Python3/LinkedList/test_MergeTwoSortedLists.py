from LinkedList.ListNodeModule import listNodeConverter, compareListNode
from LinkedList.MergeTwoSortedLists.Better021 import Solution as better

Lists = []

Lists.append([listNodeConverter([1,2,4]), listNodeConverter([1,3,4])])
Lists.append([listNodeConverter([]), listNodeConverter([1,3,4])])
Lists.append([listNodeConverter([]), listNodeConverter([])])


answer = []
answer.append(listNodeConverter([1,1,2,3,4,4]))
answer.append(listNodeConverter([1,3,4]))
answer.append(listNodeConverter([]))

def test_better():
    for i, case in enumerate(Lists):
        assert compareListNode(better().mergeTwoLists(case[0], case[1]), answer[i])