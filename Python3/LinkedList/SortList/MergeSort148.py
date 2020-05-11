# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ..ListNodeModule import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """ https://leetcode.com/problems/sort-list/discuss/613804/Python-MergeSort-Solution%3A-O(nlogn)-constant-space. """
        if not head or not head.next:
            return head

        # split list into two part
        slow = head  # will be the starting point of the second part list
        fast = head  # used to be the ending condition
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        left_list = self.sortList(head)
        right_list = self.sortList(slow)

        final_head = self.mergeList(left_list, right_list)

        return final_head

    def mergeList(self, left_list: ListNode, right_list: ListNode) -> ListNode:
        if not left_list:
            return right_list
        if not right_list:
            return left_list

        if left_list.val <= right_list.val:
            final_list = left_list
            final_list.next = self.mergeList(left_list.next, right_list)
        else:
            final_list = right_list
            final_list.next = self.mergeList(left_list, right_list.next)

        return final_list

# Runtime: 568 ms, faster than 5.11% of Python3 online submissions for Sort List.
# Memory Usage: 40.4 MB, less than 15.38% of Python3 online submissions for Sort List.


# Yet another merge sort
#
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         slow = fast = head
#         # split into half
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#         # sort each half
#         prev.next = None
#         l1 = self.sortList(head)
#         l2 = self.sortList(slow)
#         return self.mergeSort(l1, l2)
#
#     def mergeSort(self, l1, l2):
#         new_head = p = ListNode(0)
#         while l1 and l2:
#             if l1.val > l2.val:
#                 p.next=l2
#                 p = p.next
#                 l2 = l2.next
#             else:
#                 p.next = l1
#                 p = p.next
#                 l1 = l1.next
#         if l1:
#             p.next=l1
#
#         if l2:
#             p.next=l2
#
#         return new_head.next
