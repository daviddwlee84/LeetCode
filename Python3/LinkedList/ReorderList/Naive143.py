# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode
from collections import deque


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        nodes = []

        root = head
        while head:
            nodes.append(head)
            head = head.next

        nodes = deque(nodes)

        flag = True
        # just a dummy node
        previous = ListNode(-1)
        while nodes:
            if flag:
                previous.next = nodes.popleft()
            else:
                previous.next = nodes.pop()

            previous = previous.next
            flag = not flag

        previous.next = None  # make sure no cycle

        return root

# Runtime: 96 ms, faster than 59.59% of Python3 online submissions for Reorder List.
# Memory Usage: 22.3 MB, less than 7.69% of Python3 online submissions for Reorder List.
