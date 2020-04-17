class Solution:
    def checkValidString(self, s: str) -> bool:
        self.ans = False
        self.solve(0, s)
        return self.ans

    def solve(self, i: int, s: str):
        """ try all possibility for every * asterisk """
        if i == len(s):
            self.ans |= self.checkValidParentheses(s)
        elif s[i] == '*':
            for c in '() ':
                self.solve(i + 1, s[:i] + c + s[i+1:])
                if self.ans:
                    return
        else:
            self.solve(i + 1, s)

    def checkValidParentheses(self, s: str) -> bool:
        """ check string without * asterisk """
        left_parenthesis_count = 0
        for c in s:
            if c == '(':
                left_parenthesis_count += 1
            elif c == ')':
                left_parenthesis_count -= 1

            if left_parenthesis_count < 0:
                # early stop
                return False

        return left_parenthesis_count == 0
