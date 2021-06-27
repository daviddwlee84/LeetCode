class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299525/Bitmask-Hashmap
        """
        count = [1] + [0] * 1023
        mask = 0
        result = 0

        for char in word:
            mask ^= 1 << (ord(char) - ord('a'))
            result += count[mask]

            for n in range(10):
                result += count[mask ^ (1 << n)]

            count[mask] += 1

        return result

# Runtime: 3864 ms, faster than 66.67% of Python3 online submissions for Number of Wonderful Substrings.
# Memory Usage: 15.1 MB, less than 66.67% of Python3 online submissions for Number of Wonderful Substrings.
