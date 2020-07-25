# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ..ListNodeModule import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # deal with the delete root case
        while head and head.val == val:
            head = head.next

        if not head:
            return None

        root = head

        # deal with the normal case
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return root
