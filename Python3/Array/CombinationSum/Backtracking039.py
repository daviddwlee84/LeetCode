from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.backtracking(0, candidates, [], target)
        return self.answer

    def backtracking(self, current_sum: int, candidates: List[int], used: List[int], target: int):
        if current_sum == target and sorted(used) not in self.answer:
            self.answer.append(sorted(used)) # use sort to prevent duplicate set
        elif current_sum < target:
            for candidate in candidates:
                self.backtracking(current_sum+candidate, candidates, used+[candidate], target)
            