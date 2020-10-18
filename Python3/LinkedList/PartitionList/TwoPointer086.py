# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ..ListNodeModule import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        All we need is two head. One for < x and another for >= x. Then connect them together
        https://leetcode.com/problems/partition-list/discuss/29181/10-lines-concise-C%2B%2B-Solution
        https://leetcode.com/problems/partition-list/discuss/29185/Very-concise-one-pass-solution
        """
        node = head  # just for readability

        head_lt = ListNode(None)  # less than
        head_geq = ListNode(None)  # greater and equal to
        node_lt = head_lt
        node_geq = head_geq

        while node:
            if node.val < x:
                # node_lt = node_lt.next = node (You can only do this in C)
                node_lt.next = node
                node_lt = node_lt.next
            else:
                # node_geq = node_geq.next = node (You can only do this in C)
                node_geq.next = node
                node_geq = node_geq.next
            node = node.next

        node_geq.next = None
        node_lt.next = head_geq.next
        return head_lt.next

# Runtime: 32 ms, faster than 84.59% of Python3 online submissions for Partition List.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Partition List.
