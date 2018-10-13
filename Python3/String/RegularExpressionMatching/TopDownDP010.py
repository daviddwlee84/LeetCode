class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.text = s
        self.pattern = p
        self.table = {}
        return self.__dp(0, 0)
    
    # Top Down Approach
    def __dp(self, i, j):
        # It only need to calculate if dp(i, j) doesn't exist
        if (i, j) not in self.table:
            if j == len(self.pattern):
                ans = i == len(self.text)
            else:
                first_match = i < len(self.text) and self.pattern[j] in {self.text[i], '.'}
                if j+1 < len(self.pattern) and self.pattern[j+1] == '*':
                    # Consider the current p[j]p[j+1] is c* (c is char)
                    # 1. if * == 0, then skip to next p[j+1]
                    # 2. if * >= 1, check the normal situation, then check if the next s = p[j]
                    # Ps. AND will do first and then OR
                    ans = self.__dp(i, j+2) or first_match and self.__dp(i+1, j)
                else:
                    # p[j+1] is not *
                    # 1. consider the current situation and move both s and p to the next
                    ans = first_match and self.__dp(i+1, j+1)
            self.table[i, j] = ans
        return self.table[i, j]
        
