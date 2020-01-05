import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'[A-Za-z0-9]+', s))
        s = s.lower()

        print(s)

        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

# Runtime: 28 ms, faster than 99.53% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.9 MB, less than 54.76% of Python3 online submissions for Valid Palindrome.
