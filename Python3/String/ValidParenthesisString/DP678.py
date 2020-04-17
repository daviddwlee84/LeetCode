class Solution(object):
    def checkValidString(self, s):
        if not s:
            return True
        LEFTY, RIGHTY = '(*', ')*'

        # Initialize table
        # Let dp[i][j] be true if and only if the interval s[i], s[i+1], ..., s[j] can be made valid.
        # =>
        # 1. s[i] is '*' and the interval s[i+1], s[i+2], ..., s[j] can be made valid
        # 2. s[i] can be made to be '(', and there is some k in [i+1, j] such that s[k] can be made to be ')',
        #    plus the two intervals cut by s[k] (s[i+1:k] and s[k+1:j+1]) can be made valid)
        dp = [[False] * len(s) for _ in s]
        for i in range(len(s)):
            if s[i] == '*':
                dp[i][i] = True
            if i < len(s)-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in range(2, len(s)):
            for i in range(len(s) - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]
