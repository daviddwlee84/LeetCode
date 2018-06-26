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
        if not head:
            return head

        self.reverseHelper(head, None)
        return self.head
    

    def reverseHelper(self, head, last):
        nextNode = head.next
        head.next = last
        if nextNode:
            self.reverseHelper(nextNode, head)
        else:
            self.head = head

        