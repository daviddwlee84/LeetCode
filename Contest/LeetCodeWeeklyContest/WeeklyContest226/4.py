class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def isPalindrome(string: str):
            return string == string[::-1]

        for i in range(1, len(s) - 1):
            if not isPalindrome(s[:i]):
                continue
            for j in range(i + 1, len(s)):
                # print(s[:i], s[i:j], s[j:], isPalindrome(s[:i]),
                #       isPalindrome(s[i:j]), isPalindrome(s[j:]))
                if isPalindrome(s[:i]) & isPalindrome(s[i:j]) & isPalindrome(s[j:]):
                    return True
        return False
