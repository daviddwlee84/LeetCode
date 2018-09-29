class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Value = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        prev_val = 5000
        ans = 0
        for c in s:
            if prev_val >= Value[c]:
                ans += Value[c]
            else:
                ans = ans + Value[c] - 2*prev_val
            prev_val = Value[c]
        return ans
                
            