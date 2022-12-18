from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            s = 0
            num = i
            while num != 0:
                s += num % 2
                num //= 2
            ans.append(s)

        return ans
