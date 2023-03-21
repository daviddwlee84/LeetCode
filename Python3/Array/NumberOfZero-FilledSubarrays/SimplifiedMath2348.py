from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, count = 0, 0

        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            ans += count
        
        return ans
