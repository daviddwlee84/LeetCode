from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


# Runtime: 216 ms, faster than 53.27 % of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 5.81 % of Python3 online submissions for Reverse String.
