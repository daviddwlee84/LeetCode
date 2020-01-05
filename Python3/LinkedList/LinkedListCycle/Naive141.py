from ..ListNodeModule import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head not in visited:
                visited.add(head)
            else:
                return True
            head = head.next

        return False

# Runtime: 52 ms, faster than 58.52% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
