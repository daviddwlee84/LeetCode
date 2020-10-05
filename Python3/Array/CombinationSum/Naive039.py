from typing import List
from collections import Counter


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []

        def dfs(curr_list: List[int], curr_sum: int):
            if curr_sum > target:
                return
            elif curr_sum == target:
                temp = []
                for num, cnt in zip(candidates, curr_list):
                    temp.extend([num] * cnt)
                if temp not in self.answer:
                    self.answer.append(temp)
                return

            for i, num in enumerate(candidates):
                curr_list[i] += 1
                dfs(curr_list, curr_sum + num)
                curr_list[i] -= 1

        dfs([0] * len(candidates), 0)

        return self.answer
