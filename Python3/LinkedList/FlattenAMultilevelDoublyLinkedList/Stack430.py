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
        if not head:
            return head

        dummy = Node(0, None, head, None)
        stack = [head]
        prev = dummy

        while stack:
            node = stack.pop()

            # connect node popped from the stack
            node.prev = prev
            prev.next = node

            if node.next:
                stack.append(node.next)
                node.next = None
            
            if node.child:
                stack.append(node.child)
                node.child = None
        
            prev = node
        
        # remove dummy node from root
        dummy.next.prev = None
        return dummy.next

# Runtime: 40 ms, faster than 53.06% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 14.2 MB, less than 89.86% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
