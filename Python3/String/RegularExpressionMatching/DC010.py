class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        # Initial status
        # If s is not None and (pattern == s[0] or '.')
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            # Consider the current p[0]p[1] is c* (c is char)
            # 1. if * == 0, then skip to next p
            # 2. if * >= 1, check the normal situation, then check if the next s = p[0]
            # Ps. AND will do first and then OR
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            # p[1] is not *
            # 1. consider the current situation and move both s and p to the next
            return first_match and self.isMatch(s[1:], p[1:])
