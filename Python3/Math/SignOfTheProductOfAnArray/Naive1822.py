from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x: int) -> int:
            if x == 0:
                return 0
            elif x > 0:
                return 1
            else:
                return -1

        ans = 1

        # Somewhat equivalent
        # (this can avoid overflow issue in C/C++)
        #
        # for num in nums:
        #     ans *= signFunc(num)
        #
        # return ans

        for num in nums:
            ans *= num

        return signFunc(ans)
