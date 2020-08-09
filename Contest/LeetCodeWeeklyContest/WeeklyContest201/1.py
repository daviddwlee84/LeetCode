class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and (s[i] == s[i + 1].upper() or s[i] == s[i + 1].lower()):
                s = self.makeGood(s[:i] + s[i+2:])
                break

        return s
