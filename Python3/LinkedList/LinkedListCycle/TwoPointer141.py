from ..ListNodeModule import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slowPointer = head
        fastPointer = head.next

        # Consider a cyclic list. The fast runner will eventually meet the slow runner.
        while slowPointer != fastPointer:
            if fastPointer is None or fastPointer.next is None:
                # If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.
                return False

            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        return True

# Runtime: 48 ms, faster than 78.97% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
