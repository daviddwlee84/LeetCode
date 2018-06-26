from LinkedList.ReverseLinkedList.Iterative206 import Solution as iterative
from LinkedList.ReverseLinkedList.Recursive206 import Solution as recursive
from LinkedList.ListNodeModule import compareListNode, listNodeConverter

linkedlist = []
linkedlist.append(listNodeConverter([1, 2, 3, 4, 5]))
linkedlist.append(listNodeConverter([1]))
linkedlist.append(listNodeConverter([]))

answer = []
answer.append(listNodeConverter([5, 4, 3, 2, 1]))
answer.append(listNodeConverter([1]))
answer.append(listNodeConverter([]))

def test_iterative():
    for i, ll in enumerate(linkedlist):
        assert compareListNode(iterative().reverseList(ll), answer[i]) == True

linkedlist2 = []
linkedlist2.append(listNodeConverter([1, 2, 3, 4, 5]))
linkedlist2.append(listNodeConverter([1]))
linkedlist2.append(listNodeConverter([]))

def test_recursive():
    for i, ll in enumerate(linkedlist2):
        assert compareListNode(recursive().reverseList(ll), answer[i]) == True