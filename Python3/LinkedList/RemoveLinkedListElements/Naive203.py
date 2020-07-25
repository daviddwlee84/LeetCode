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

# 2020/7/20
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         dummy = ListNode(next=head)
#         prev = dummy
#         node = head
#         while node:
#             if node.val == val:
#                 prev.next = node.next
#             else:
#                 prev = node
#             node = node.next
#
#         return dummy.next
