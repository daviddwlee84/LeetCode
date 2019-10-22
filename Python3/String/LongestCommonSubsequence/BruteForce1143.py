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

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        if len(text1) < len(text2):
            # make sure text1 is the longer string
            text2, text1 = text1, text2

        max_len = 0
        # enumerate all subsequences of text2
        for i in range(1, 2**len(text2)):
            text2_subseq = self.getSubsequenceByBinaryNum(i, text2)
            if self.checkIfSubsequenceInText(text2_subseq, text1):
                max_len = max(max_len, len(text2_subseq))

        return max_len

    def checkIfSubsequenceInText(self, subseq: str, text: str) -> bool:
        i = j = 0
        while i < len(subseq) and j < len(text):
            if subseq[i] == text[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if i != len(subseq):
            return False
        else:
            return True
            
    def getSubsequenceByBinaryNum(self, num: int, text: str) -> str:
        subseq = ''
        i = 0
        while num > 0:
            if num & 1:
                subseq += text[i]
            num = num >> 1
            i += 1
        return subseq

# Time Limit Exceeded
# 13/37 cases passed (N/A)