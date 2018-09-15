class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dic = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in dic:
                stack.append(char)
            elif not stack or dic[stack.pop()] != char:
                return False
        return not stack