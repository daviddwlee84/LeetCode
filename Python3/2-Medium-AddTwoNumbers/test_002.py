import ListNode as ln

from Naive002 import Solution as naive

def test_naive():
    l1 = ln.listNodeConverter([2, 4, 3])
    l2 = ln.listNodeConverter([5, 6, 4])
    ans = ln.listNodeConverter([7, 0, 8])
    assert ln.compareListNode(ans, naive().addTwoNumbers(l1, l2)) == True

    l1 = ln.listNodeConverter([1, 8])
    l2 = ln.listNodeConverter([0])
    ans = ln.listNodeConverter([1, 8])
    assert ln.compareListNode(ans, naive().addTwoNumbers(l1, l2)) == True