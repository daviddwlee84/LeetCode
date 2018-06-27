# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        totalLists = len(lists)
        interval = 1

        """
        0  1 2  3 4  5  <= Interval = 1
        | /  | /  | /
        0    2    4     <= Interval = 2
        |  /      |
        0         4     <= Interval = 4
        |      /
        0               <= Interval = 8 > totalLists = 5
        """
        while interval < totalLists:
            for i in range(0, totalLists - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])

            interval *= 2
        
        return lists[0] if totalLists > 0 else lists
    
    def merge2Lists(self, l1, l2):
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