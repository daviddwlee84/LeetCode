class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        https://leetcode.com/problems/power-of-four/discuss/80457/Java-1-line-(cheating-for-the-purpose-of-not-using-loops)
        https://leetcode.com/problems/power-of-four/discuss/80460/1-line-C%2B%2B-solution-without-confusing-bit-manipulations
        https://leetcode.com/problems/power-of-four/discuss/80456/O(1)-one-line-solution-without-loops
        https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
        """
        return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) == num

# Runtime: 36 ms, faster than 51.59% of Python3 online submissions for Power of Four.
# Memory Usage: 13.8 MB, less than 57.02% of Python3 online submissions for Power of Four.
