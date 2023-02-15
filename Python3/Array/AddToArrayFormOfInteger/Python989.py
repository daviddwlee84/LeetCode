from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(c) for c in str(int(''.join(str(n) for n in num)) + k)]
