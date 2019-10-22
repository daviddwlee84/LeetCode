# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.17%)
# Likes:    275
# Dislikes: 8
# Total Accepted:    16.3K
# Total Submissions: 28.4K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
# 
# 
# 
# If there is no common subsequence, return 0.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.

import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        self.X, self.Y = text1, text2

        # the column and row 0 is the initial value
        self.c = np.full((m+1, n+1), -1) # m x n
        self.c[:, 0] = 0
        self.c[0, :] = 0
        # table used to construct LCS (not necessary for the max length)
        self.b = np.full((m, n), '', dtype=str)

        for i in range(m):
            for j in range(n):
                if self.X[i] == self.Y[j]:
                    # find same char
                    # copy the top left count
                    self.c[i+1, j+1] = self.c[i, j] + 1
                    self.b[i, j] = '↖'
                elif self.c[i, j+1] >= self.c[i+1, j]:
                    # if top count is greater
                    # copy the top count
                    self.c[i+1, j+1] = self.c[i, j+1]
                    self.b[i, j] = '↑'
                else:
                    # if left count is greater
                    # copy the left count
                    self.c[i+1, j+1] = self.c[i+1, j]
                    self.b[i, j] = '←'

        return self.c[m, n]
    
# 37/37 cases passed (1128 ms)
# Your runtime beats 9.93 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (41.5 MB)

    def printLCS(self, i: int, j: int):
        if i == 0 or j == 0:
            return
        print(self.b[i-1, j-1])
        if self.b[i-1, j-1] == '↖':
            # backtrack the chars with ↖
            self.printLCS(i-1, j-1)
            print(self.X[i-1], end='')
        elif self.b[i-1, j-1] == '↑':
            self.printLCS(i-1, j)
        else:
            self.printLCS(i, j-1)

if __name__ == "__main__":
    # text book case
    case = Solution()
    case.longestCommonSubsequence('ABCBDAB', 'BDCABA')
    print(case.c)
    print(case.b)
    case.printLCS(len('ABCBDAB'), len('BDCABA'))
