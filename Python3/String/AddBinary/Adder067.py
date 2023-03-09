from typing import Tuple

# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (40.68%)
# Likes:    1198
# Dislikes: 224
# Total Accepted:    350.3K
# Total Submissions: 854.8K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # fill the leading zeros
        max_len = max(len(a), len(b))
        if len(a) < max_len:
            a = '0'*(max_len-len(a)) + a
        if len(b) < max_len:
            b = '0'*(max_len-len(b)) + b
        
        answer = ''
        carry = 0
        for i in range(max_len-1, -1, -1):
            result, carry = self.adder(int(a[i]), int(b[i]), carry)
            answer = str(result) + answer
        if carry != 0:
            answer = str(carry) + answer
        
        return answer
    
    def adder(self, a: int, b: int, carry: int) -> Tuple[int, int]:
        # can be written in combination logic
        result = a + b + carry
        if result < 2:
            return result, 0
        elif result == 2:
            return 0, 1
        elif result == 3:
            return 1, 1

# 294/294 cases passed (48 ms)
# Your runtime beats 19.66 % of python3 submissions
# Your memory usage beats 5.41 % of python3 submissions (13.8 MB)