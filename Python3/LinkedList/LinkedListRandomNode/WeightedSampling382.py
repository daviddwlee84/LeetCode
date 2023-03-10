from typing import Optional
import numpy as np
from ..ListNodeModule import ListNode
from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.counter = defaultdict(int)
        self.n = 0
        while head:
            self.counter[head.val] += 1
            self.n += 1
            head = head.next
        for key in self.counter:
            self.counter[key] /= self.n

    def getRandom(self) -> int:
        return np.random.choice(list(self.counter.keys()), size=1, p=list(self.counter.values()))[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
