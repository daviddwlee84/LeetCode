from typing import List
from math import trunc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                token1 = stack.pop()
                token2 = stack.pop()
                calc = 0
                if token == '+':
                    calc = token2 + token1
                elif token == '-':
                    calc = token2 - token1
                elif token == '*':
                    calc = token2 * token1
                elif token == '/':
                    calc = trunc(token2 / token1)
                stack.append(calc)
            else:
                stack.append(int(token))

        return stack.pop()

# Runtime: 64 ms, faster than 86.73% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Evaluate Reverse Polish Notation.
