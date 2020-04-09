from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.getString(S) == self.getString(T)

    def getString(self, string: str) -> List[str]:
        stack = []
        for c in string:
            if len(stack) > 0 and c == '#':
                stack.pop()
            elif c != '#':
                stack.append(c)
        return stack
