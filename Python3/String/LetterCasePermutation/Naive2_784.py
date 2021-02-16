from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.answer = []

        def dfs(i: int, curr_chars: str):
            if i == len(S):
                self.answer.append(curr_chars)
                return
            if ord('0') <= ord(S[i]) <= ord('9'):
                dfs(i + 1, curr_chars + S[i])
            else:
                dfs(i + 1, curr_chars + S[i].lower())
                dfs(i + 1, curr_chars + S[i].upper())
        dfs(0, '')
        return self.answer
