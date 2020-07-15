from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = nums
        self.dfs([])
        return self.answer

    def dfs(self, curr: List[int]):
        if len(curr) == len(self.nums):
            self.answer.append(
                [item for to_pick, item in zip(curr, self.nums) if to_pick])
            return

        self.dfs(curr + [False])
        self.dfs(curr + [True])
