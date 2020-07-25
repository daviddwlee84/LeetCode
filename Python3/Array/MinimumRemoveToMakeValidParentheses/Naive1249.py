class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer = []
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                if balance > 0:
                    balance -= 1
                else:
                    continue
            answer.append(char)

        if balance == 0:
            return ''.join(answer)
        else:
            final_answer = []
            for char in reversed(answer):
                if char == '(' and balance > 0:
                    balance -= 1
                    continue
                final_answer.append(char)
            return ''.join(reversed(final_answer))

# Runtime: 208 ms, faster than 26.44% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 17.6 MB, less than 5.26% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
