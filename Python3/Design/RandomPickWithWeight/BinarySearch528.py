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
        Binary Search
        """
        num = random.random() * self.max_num
        left, right = 0, len(self.cum_sum)
        while left < right:
            mid = left + (right - left) // 2
            if self.cum_sum[mid] < num <= self.cum_sum[mid + 1]:
                return mid
            elif self.cum_sum[mid] >= num:
                right = mid
            else:
                left = mid + 1

        return left

# Runtime: 280 ms, faster than 53.25% of Python3 online submissions for Random Pick with Weight.
# Memory Usage: 18.7 MB, less than 36.74% of Python3 online submissions for Random Pick with Weight.
