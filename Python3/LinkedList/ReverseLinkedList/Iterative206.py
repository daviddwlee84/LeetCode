# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastNode = None
        while head:
            nextNode = head.next
            head.next = lastNode
            lastNode = head
            head = nextNode
        
        return lastNode
            