class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        HashSet = set() # HashSet to check if a character in the current
        
        ans = 0
        start = end = 0 # Indices

        while start < n and end < n:
            if s[end] not in HashSet:
                HashSet.add(s[end])
                end += 1
                ans = max(ans, end - start)
            else:
                # If find the repeating character, move the start index forward
                HashSet.remove(s[start])
                start += 1
        
        return ans