from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        https://leetcode.com/problems/validate-stack-sequences/solutions/1853250/java-c-space-complexity-going-from-o-n-o-1/
        """
        i = 0
        j = 0
        for num in pushed:
            # Using pushed as the stack
            pushed[i] = num
            i += 1

            while i > 0 and pushed[i - 1] == popped[j]:
                i -= 1
                j += 1

        return i == 0
