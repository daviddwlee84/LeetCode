from ..ListNodeModule import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for _ in range(n):
            fast = fast.next

        slow = head

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        if not prev:
            if not slow:
                # only one element => become empty
                return None
            else:
                # delete the first node
                return slow.next

        prev.next = prev.next.next

        return head

# Runtime: 44 ms, faster than 34.05% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 71.73% of Python3 online submissions for Remove Nth Node From End of List.
