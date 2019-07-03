class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if haystack == needle:
            index = 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    index = i
                    break
        return index
