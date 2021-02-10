# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        original_list = []
        new_list = []

        # Create new nodes
        while head:
            original_list.append(head)
            new_node = Node(head.val)
            new_list.append(new_node)
            head = head.next

        # Construct next and random pointer
        for ori_node, new_node in zip(original_list, new_list):
            if ori_node.next:
                # otherwise leave it as None
                next_idx = original_list.index(ori_node.next)
                new_node.next = new_list[next_idx]
            if ori_node.random:
                random_idx = original_list.index(ori_node.random)
                new_node.random = new_list[random_idx]

        return new_list[0]

# Runtime: 44 ms, faster than 21.22% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15.2 MB, less than 29.95% of Python3 online submissions for Copy List with Random Pointer.
