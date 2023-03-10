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
        """
        https://leetcode.com/problems/linked-list-random-node/solutions/3278243/java-using-reservoir-sampling/
        https://en.wikipedia.org/wiki/Reservoir_sampling
        """
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        counter = 0
        result = None
        while node:
            counter += 1

            # Equivalent
            # if random.randint(1, counter) == 1:
            if int(random.random() * counter) == 0:
                # update result
                result = node.val
            node = node.next
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
