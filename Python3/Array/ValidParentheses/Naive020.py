class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        openBrackets = ['(', '[', '{']
        closeBrackets = [')', ']', '}']

        stack = []

        for char in s:
            if char in openBrackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    # Encounter close bracket when there is no open bracket in front
                    return False
                if closeBrackets[openBrackets.index(stack.pop())] != char:
                    return False
        if len(stack) == 0:
            return True
        else:
            # There is some open bracket haven't been paired
            return False
