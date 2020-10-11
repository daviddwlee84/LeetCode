class Solution:
    def maxDepth(self, s: str) -> int:
        """
        It is guaranteed that parentheses expression s is a VPS.
        """
        count = 0
        maximum = 0
        for c in s:
            maximum = max(maximum, count)
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return maximum
