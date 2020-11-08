from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.cum_sum = [0]
        for num in w:
            self.cum_sum.append(self.cum_sum[-1] + num)
        self.max_num = self.cum_sum[-1]

    def pickIndex(self) -> int:
        """
        Linear
        """
        num = random.random() * self.max_num
        for i, s in enumerate(self.cum_sum):
            if num <= s:
                return i - 1

# Runtime: 6580 ms, faster than 11.31% of Python3 online submissions for Random Pick with Weight.
# Memory Usage: 18.3 MB, less than 36.74% of Python3 online submissions for Random Pick with Weight.
