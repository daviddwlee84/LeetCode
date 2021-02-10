# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        # store the visited node
        self.dic = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Treat linked list as a graph
        """
        if head is None:
            return None

        if head in self.dic:
            return self.dic[head]

        node = Node(head.val, None, None)
        self.dic[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return self.dic[head]

# Runtime: 36 ms, faster than 68.57% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15.5 MB, less than 13.49% of Python3 online submissions for Copy List with Random Pointer.


# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return None
#
#         hash_table = dict()
#         m = n = head
#
#         while m:
#             hash_table[m] = Node(m.val)
#             m = m.next
#
#         while n:
#             hash_table[n].next = hash_table.get(n.next)
#             hash_table[n].random = hash_table.get(n.random)
#             n = n.next
#
#         return hash_table[head]
