from LinkedList.ListNodeModule import listNodeConverter, compareListNode
from LinkedList.RemoveNthNodeFromEndOfList.HT019 import Solution as HashTable
from LinkedList.RemoveNthNodeFromEndOfList.TwoPointer019 import Solution as TwoPointer

linkedlist = []
linkedlist.append([1, 2, 3, 4, 5])
linkedlist.append([1])
linkedlist.append([1, 2])

n = []
n.append(2)
n.append(1)
n.append(2)

answer = []
answer.append(listNodeConverter([1, 2, 3, 5]))
answer.append(listNodeConverter([]))
answer.append(listNodeConverter([2]))

def test_hashtable():
    for i, ll in enumerate(linkedlist):
        assert compareListNode(HashTable().removeNthFromEnd(listNodeConverter(ll), n[i]), answer[i]) == True

def test_twopointer():
    for i, ll in enumerate(linkedlist):
        assert compareListNode(TwoPointer().removeNthFromEnd(listNodeConverter(ll), n[i]), answer[i]) == True
