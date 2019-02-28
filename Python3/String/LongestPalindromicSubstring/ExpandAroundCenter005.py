class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        self.s = s
        self.longest = ""

        for center in range(len(s)):
            self.expandAroundCenter(center, center) # odd case
            self.expandAroundCenter(center, center+1) # even case
            
        return self.longest
    
    def expandAroundCenter(self, left: int, right: int):
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            # if the indices is still in range
            # and the characters surrounding are the same
            left -= 1; right += 1 # try next one
        
        current_longest = self.s[left+1:right] # (left may be -1)
        if len(current_longest) > len(self.longest):
            self.longest = current_longest
