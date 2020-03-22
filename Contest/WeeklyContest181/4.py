class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in reversed(range(len(s))):
            if s[:i] == s[-i:]:
                return s[:i]
        return ''


if __name__ == "__main__":
    print(Solution().longestPrefix('level'), 'l')
    print(Solution().longestPrefix('ababab'), 'abab')
    print(Solution().longestPrefix('leetcodeleet'), 'leet')
    print(Solution().longestPrefix('a'), '')
    print(Solution().longestPrefix('aaaaa'), 'aaaa')
