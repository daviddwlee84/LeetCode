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
        if not root:
            return root

        # maintain tree pointer
        parent = root
        childHead = None
        child = None

        while parent:
            while parent:
                # check left child
                if parent.left:
                    if not childHead:  # reach new level
                        childHead = parent.left
                    else:  # just concatenate to the current linked list
                        child.next = parent.left
                    child = parent.left  # moving forward (child)

                # do the same thing on right child
                if parent.right:
                    if not childHead:  # reach new level
                        childHead = parent.right
                    else:  # just concatenate to the current linked list
                        child.next = parent.right
                    child = parent.right  # moving forward (child)

                parent = parent.next  # moving forward (parent)

            # go to next level
            parent = childHead
            child = None
            childHead = None

        return root

# Runtime: 36 ms, faster than 99.74% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
