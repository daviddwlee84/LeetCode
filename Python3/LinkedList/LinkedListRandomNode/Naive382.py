from typing import Optional
import random
from ..ListNodeModule import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.list = []
        while head:
            self.list.append(head)
            head = head.next

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.list) - 1)
        return self.list[idx].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
