class Solution:
    def removeDuplicates(self, s: str) -> str:
        found = True
        while found and len(s) >= 2:
            found = False
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    s = s[:i] + s[i + 2:]
                    found = True
                    break

        return s

# Runtime: 7524 ms, faster than 5.01% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.6 MB, less than 81.74% of Python3 online submissions for Remove All Adjacent Duplicates In String.
