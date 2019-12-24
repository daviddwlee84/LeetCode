"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:  # only single or no node
            return root

        # connect children of current node
        root.left.next = root.right

        # (key point)
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

# Runtime: 64 ms, faster than 72.85% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.
