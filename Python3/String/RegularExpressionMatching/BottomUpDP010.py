class Solution:
    # Bottom Up Approach
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # Initialize the table to all False
        # size = length of s (rows) * length of p (cols)
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True # Empty string and pattern must be True

        # Compare the string from the last element
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1): # Leave the space for * (if any)
                first_match = i < len(s) and p[j] in {s[i], '.'} # make sure i is in range
                if j+1 < len(p) and p[j+1] == '*':
                    # Consider the current p[j]p[j+1] is c* (c is char)
                    # 1. if * == 0, then skip to next p[j+1]
                    # 2. if * >= 1, check the normal situation, then check if the next s = p[j]
                    # Ps. AND will do first and then OR
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    # p[j+1] is not *
                    # 1. consider the current situation and move both s and p to the next
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
