from typing import List, Optional
from ..ListNodeModule import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/merge-k-sorted-lists/solutions/3286803/python3-and-c-95-ms-beats-95-60-and-easy/
        """
        values = []
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next

        values.sort()
        dummy_head = ListNode(None)
        node = dummy_head
        for val in values:
            node.next = ListNode(val)
            node = node.next
        return dummy_head.next
