from LinkedList.ListNodeModule import listNodeConverter, compareListNode

from LinkedList.AddTwoNumbers.Naive002 import Solution as naive

def test_naive():
    l1 = listNodeConverter([2, 4, 3])
    l2 = listNodeConverter([5, 6, 4])
    ans = listNodeConverter([7, 0, 8])
    assert compareListNode(ans, naive().addTwoNumbers(l1, l2)) == True

    l1 = listNodeConverter([1, 8])
    l2 = listNodeConverter([0])
    ans = listNodeConverter([1, 8])
    assert compareListNode(ans, naive().addTwoNumbers(l1, l2)) == True