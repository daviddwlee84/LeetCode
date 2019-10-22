# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (43.44%)
# Likes:    952
# Dislikes: 87
# Total Accepted:    373.8K
# Total Submissions: 857.8K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        appear = set()
        node = head
        last = head
        while node:
            if node.val in appear:
                # delete current node
                last.next = node.next
                # last node remain same node
            else:
                appear.add(node.val)
                last = node
            # next node
            node = node.next
        return head
 
# 165/165 cases passed (108 ms)
# Your runtime beats 7.6 % of python3 submissions
# Your memory usage beats 6.45 % of python3 submissions (13.8 MB)