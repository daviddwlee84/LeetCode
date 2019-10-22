# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.16%)
# Likes:    923
# Dislikes: 1557
# Total Accepted:    430.9K
# Total Submissions: 1.3M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for i in range(1, x):
            if i*i < x:
                less = i
            elif i*i == x:
                return i
            else:
                return less
        return less

# 1017/1017 cases passed (1820 ms)
# Your runtime beats 6.07 % of python3 submissions
# Your memory usage beats 6.45 % of python3 submissions (14 MB)