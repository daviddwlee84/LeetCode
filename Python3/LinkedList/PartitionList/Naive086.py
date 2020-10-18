# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ..ListNodeModule import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node = head

        parent_geq_node = None
        first_geq_node = None
        geq_node = None
        while node:
            if not first_geq_node:
                if node.next and node.next.val >= x:
                    parent_geq_node = node
                    first_geq_node = node.next
                    geq_node = node.next
            elif node != first_geq_node:
                if node.val < x:
                    parent_geq_node.next = node
                    parent_geq_node = parent_geq_node.next
                else:
                    geq_node.next = node
                    geq_node = geq_node.next
            node = node.next

        if parent_geq_node:
            parent_geq_node.next = first_geq_node
            if geq_node:
                geq_node.next = None

        return head

# WA
#
# [2,1]
# 2
#
# [1,2]
