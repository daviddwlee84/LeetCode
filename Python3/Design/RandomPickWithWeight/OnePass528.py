from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        """
        Constraint: You can only pass one time at each pickIndex() call
        """
        curr_sum = 0
        answer = 0
        for i, num in enumerate(self.w):
            curr_sum += num
            if random.random() <= num / curr_sum:
                answer = i
        return answer
