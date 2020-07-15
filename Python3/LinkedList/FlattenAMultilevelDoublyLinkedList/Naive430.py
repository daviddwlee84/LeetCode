"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        while node:
            if node.child:
                child_node = node.child
                # find the tail of child
                while child_node:
                    child_prev = child_node
                    child_node = child_node.next
                # connect end of child to next node
                if node.next:
                    # node.next might be None
                    node.next.prev = child_prev
                child_prev.next = node.next
                # connect node to head of child
                node.next = node.child
                node.child.prev = node
                node.child = None

            node = node.next

        return head

# Runtime: 28 ms, faster than 97.13% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 14.3 MB, less than 68.30% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
