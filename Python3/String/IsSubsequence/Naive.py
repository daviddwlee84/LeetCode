class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            while s[i] != t[j]:
                j += 1
                if j >= len(t):
                    break

            if j >= len(t):
                break

            # s[i] == t[j]
            i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False
