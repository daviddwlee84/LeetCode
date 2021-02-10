# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        This take O(1) space
        """
        if not head:
            return None

        node = head
        while node:
            new_node = Node(node.val)
            # connect new node right after the original node
            new_node.next = node.next
            node.next = new_node

            node = node.next.next

        # assign random
        node = head
        while node:
            new_node = node.next
            if node.random:
                # otherwise leave it as None
                new_node.random = node.random.next
            node = node.next.next

        # deal with next
        node = head
        while node:
            new_node = node.next
            next_node = node.next.next
            if next_node:
                # otherwise leave it as None
                new_node.next = node.next.next.next
            node = next_node

        return head.next

# Runtime: 36 ms, faster than 68.57% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.8 MB, less than 96.39% of Python3 online submissions for Copy List with Random Pointer.
