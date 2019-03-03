from LinkedList.ListNodeModule import listNodeConverter, compareListNode
from LinkedList.RemoveNthNodeFromEndOfList.HT019 import Solution as HashTable

linkedlist = []
linkedlist.append(listNodeConverter([1, 2, 3, 4, 5]))
linkedlist.append(listNodeConverter([1]))

n = []
n.append(2)
n.append(1)

answer = []
answer.append(listNodeConverter([1, 2, 3, 5]))
answer.append(listNodeConverter([]))

def test_hashtable():
    for i, ll in enumerate(linkedlist):
        assert compareListNode(HashTable().removeNthFromEnd(ll, n[i]), answer[i]) == True
