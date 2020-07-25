from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/single-number-iii/discuss/701198/Python-Find-the-difference-between-the-two-numbers-then-use-last-1-as-discriminator
        https://medium.com/@Bear_/260-single-number-iii-d35b7cc0e0aa
        https://www.cnblogs.com/grandyang/p/4741122.html

        [1,2,1,3,2,5]
        """
        diff = 0
        for num in nums:
            diff ^= num

        # diff = 3 ^ 5 = 6

        # get the right most '1' bit (actually we can just use any '1' bit)
        # equivalent: diff & (~ (diff - 1))
        discriminator = diff & (-diff)

        # 6 = 0110
        # -6 = ~(6-1) = 1010
        #
        # discriminator = 0110 & 1010 = 0010 = 2

        # 3 & 2 == 1
        # 5 & 2 == 0

        # method 1:
        # answer = [0, 0]
        # for num in nums:
        #     if num & discriminator:
        #         answer[0] ^= num
        #     else:
        #         answer[1] ^= num
        # return answer

        # method 2:
        single1 = 0
        for num in nums:
            if num & discriminator:
                single1 ^= num

        return [single1, single1 ^ diff]

# Runtime: 52 ms, faster than 96.37% of Python3 online submissions for Single Number III.
# Memory Usage: 15.3 MB, less than 80.52% of Python3 online submissions for Single Number III.
