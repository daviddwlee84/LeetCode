from typing import List
import sys


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        return self._recursive(-sys.maxsize, 0)

    def _recursive(self, prev_num: int, curr_pos: int) -> int:
        if (curr_pos == len(self.nums)):
            return 0  # reach the end of the list

        taken = 0
        curr_num = self.nums[curr_pos]
        if curr_num > prev_num:
            # take current num
            taken = 1 + self._recursive(curr_num, curr_pos + 1)

        # max length of including current num or not
        return max(taken, self._recursive(prev_num, curr_pos + 1))
