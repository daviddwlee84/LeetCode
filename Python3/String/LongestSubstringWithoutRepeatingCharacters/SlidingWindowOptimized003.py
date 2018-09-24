class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        HashMap = {} # Store current index of character
        
        ans = 0

        start = 0
        for end in range(n):
            if s[end] in HashMap:
                # If find the repeating character, use it as a new start point
                start = max(HashMap[s[end]], start)
            ans = max(ans, end - start + 1)
            HashMap[s[end]] = end + 1
        
        return ans