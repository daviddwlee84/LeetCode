class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            ans += 1
        return ans
            
# Runtime: 32 ms, faster than 56.81% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.7 MB, less than 81.80% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/502809/just-count-number-of-0-and-1-in-binary
