from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []

        def dfs(left, right, tmp):
            if not left and not right:
                answer.append(''.join(tmp))
                return
            if left:
                dfs(left - 1, right, tmp + ['('])
            if right and left < right:
                dfs(left, right - 1, tmp + [')'])

        dfs(n, n, [])
        return answer

# Runtime: 44 ms, faster than 38.50% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.2 MB, less than 13.99% of Python3 online submissions for Generate Parentheses.
