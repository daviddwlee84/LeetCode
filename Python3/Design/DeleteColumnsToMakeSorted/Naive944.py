from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        to_delete = 0
        n = len(strs[0])
        # For each columns
        for i in range(n):
            temp = None
            for string in strs:
                if temp and ord(string[i]) < ord(temp):
                    to_delete += 1
                    break
                temp = string[i]

        return to_delete
