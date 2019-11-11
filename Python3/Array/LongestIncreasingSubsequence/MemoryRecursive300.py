from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = [[None for _ in range(len(nums))] for _ in range(len(nums) + 1)]
        return self._recursive(-1, 0)
    
    def _recursive(self, prev_pos: int, curr_pos: int) -> int:
        if curr_pos == len(self.nums):
            return 0
        
        # only calculate when whe memory is empty
        if self.memo[prev_pos + 1][curr_pos] is None:
            taken = 0
            if prev_pos < 0 or self.nums[curr_pos] > self.nums[prev_pos]:
                taken = 1 + self._recursive(curr_pos, curr_pos + 1)
            nottaken = self._recursive(prev_pos, curr_pos + 1)
            self.memo[prev_pos + 1][curr_pos] = max(taken, nottaken)

        return self.memo[prev_pos + 1][curr_pos]
