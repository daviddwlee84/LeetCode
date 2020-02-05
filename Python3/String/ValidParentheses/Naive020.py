class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in open_brackets: # open bracket
                stack.append(c)
            else: # close brakcet
                if len(stack) == 0:
                    # if nothing to pop then it must be invalid
                    return False
                open_bracket = stack.pop()    
                if open_brackets[open_bracket] != c:
                    return False
        if len(stack) == 0:
            return True        
        else:
            return False
