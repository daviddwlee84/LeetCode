from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.backtracking("", 0, 0, n)
        return self.answer
    
    def backtracking(self, string: str, left: int, right: int, n: int):
        if len(string) == n*2:
            self.answer.append(string)
        
        # The order of these two if condition doesn't matter
        if right < left:
            self.backtracking(string + ')', left, right+1, n)
        if left < n:
            self.backtracking(string + '(', left+1, right, n)
