# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fakeRoot = ListNode(-1)
        fakeRoot.next = head

        previous = fakeRoot
        while head is not None:
            if head.val == val:
                # delete node
                previous.next = head.next
            else:
                # or forward previous pointer
                previous = head
            head = head.next

        return fakeRoot.next
