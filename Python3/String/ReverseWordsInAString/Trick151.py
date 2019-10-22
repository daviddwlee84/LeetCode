# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (17.94%)
# Likes:    686
# Dislikes: 2464
# Total Accepted:    321.5K
# Total Submissions: 1.8M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# 
# 
# Example 1:
# 
# 
# Input: "the sky is blue"
# Output: "blue is sky the"
# 
# 
# Example 2:
# 
# 
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
# 
# 
# Example 3:
# 
# 
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
# 
# 
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# 
# 
# Follow up:
# 
# For C programmers, try to solve it in-place in O(1) extra space.

from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip() # this will only remove the leading and trailing spaces
        s = ' '.join(s.split()) # same as s = re.sub(r'\s{2,}', ' ', s}
        charList = list(s)
        begin = 0
        while begin < len(s):
            if charList[begin] == ' ':
                begin += 1
                continue
            else:
                end = begin
                while end < len(s) and charList[end] != ' ':
                    end += 1
                self.reverse(begin, end, charList)
                begin = end
        self.reverse(0, len(s), charList)
        print(''.join(charList))
        return ''.join(charList)

    def reverse(self, begin: int, end: int, charList: List):
        for i in range(begin, (begin+end)//2):
            charList[i], charList[begin+end-i-1] = charList[begin+end-i-1], charList[i]

# 25/25 cases passed (88 ms)
# Your runtime beats 5.14 % of python3 submissions
# Your memory usage beats 8.7 % of python3 submissions (14.5 MB)