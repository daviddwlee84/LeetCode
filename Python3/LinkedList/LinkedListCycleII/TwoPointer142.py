from ..ListNodeModule import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                found = True
                break

        if not found:
            return None

        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

# Runtime: 56 ms, faster than 42.73% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.1 MB, less than 18.78% of Python3 online submissions for Linked List Cycle II.
