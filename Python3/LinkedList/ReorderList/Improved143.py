# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return

        # 1. Find the mid point
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Cut the mid point
        mid = slow.next
        slow.next = None

        # 2. Reverse the second half
        pre = None  # this is the reversed list's root
        while mid:
            mid.next, pre, mid = pre, mid, mid.next

        # 3. Mix the halves
        while pre:
            head.next, pre.next, pre, head = pre, head.next, pre.next, head.next

# Runtime: 96 ms, faster than 59.59% of Python3 online submissions for Reorder List.
# Memory Usage: 22.2 MB, less than 7.69% of Python3 online submissions for Reorder List.
