from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        https://leetcode.com/problems/validate-stack-sequences/solutions/1853250/java-c-space-complexity-going-from-o-n-o-1/
        """
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])

            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack
