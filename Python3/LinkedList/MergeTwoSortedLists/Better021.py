# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Declare a temporary head, because we aren't sure l1 or l2 is None or Head
        tempHead = node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if not l1:
            # If l1 is empty, then connect the rest of l2 to node
            node.next = l2
        else:
            # Vice versa
            node.next = l1
        return tempHead.next

        