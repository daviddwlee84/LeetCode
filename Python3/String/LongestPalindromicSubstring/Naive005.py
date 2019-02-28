class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        longest = ""

        for length in range(1, len(s)+1):
            for start in range(len(s)-length+1):
                if self.testPalindrome(s[start:start+length]):
                    longest = s[start:start+length]
        return longest

    def testPalindrome(self, s: str) -> bool:
        half = len(s)//2
        for i in range(half):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
