from typing import List, Optional
from ..ListNodeModule import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/merge-k-sorted-lists/solutions/3285977/hard-made-it-easy-easily-explained-by-divide-and-conquer-method/
        """
        if not lists:
            return None
        
        return self.merge_lists_two_by_two(lists, 0, len(lists) - 1)
        
    def merge_lists_two_by_two(self, lists: List[Optional[ListNode]], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        left_lists = self.merge_lists_two_by_two(lists, start, mid)
        right_lists = self.merge_lists_two_by_two(lists, mid + 1, end)
        return self.merge_two_lists(left_lists, right_lists)
    
    def merge_two_lists(self, left_head: ListNode, right_head: ListNode):
        node = dummy_head = ListNode(None)
        while left_head and right_head:
            # Connect smaller one 
            if left_head.val < right_head.val:
                node.next = left_head
                left_head = left_head.next
            else:
                node.next = right_head
                right_head = right_head.next
            node = node.next
        
        # Connect the rest of the sorted list (either is left or right)

        # while left_head:
        #     node.next = left_head
        #     left_head = left_head.next
        #     node = node.next
        # while right_head:
        #     node.next = right_head
        #     right_head = right_head.next
        #     node = node.next

        # Equivalent
        if left_head:
            node.next = left_head
        elif right_head:
            node.next = right_head
        
        return dummy_head.next
