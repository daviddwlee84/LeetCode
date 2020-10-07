from ..ListNodeModule import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        nodes = []
        i = 0
        node = head
        while node:
            nodes.append(node)
            node = node.next
            i += 1

        if i <= 1:
            return head

        total_length = i
        k %= total_length

        if k == 0:
            return head

        nodes[-k-1].next = None
        nodes[-1].next = nodes[0]
        return nodes[-k]
