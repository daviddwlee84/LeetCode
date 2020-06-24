from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/single-number-ii/discuss/699858/Algorithm-Explained-or-Beginner-Friendly-or-Example-Dry-Run-or-Bitwise-Solution-or-Brute-Force

        Three cases
        1. A new number appears: XOR it into `ones`
        2. A number repeated (appears twice): remove from `ones` and XOR it into `twos`
        3. A number appears for the third time: remove from both `ones` and `twos`
        """
        ones = 0
        twos = 0
        not_threes = 0

        for num in nums:

            # for case 1. and 2.
            twos |= (ones & num)
            ones ^= num

            # remove common 1's bits from ones and twos
            not_threes = ~(ones & twos)
            ones &= not_threes
            twos &= not_threes

        return ones

# Runtime: 60 ms, faster than 58.41% of Python3 online submissions for Single Number II.
# Memory Usage: 15.4 MB, less than 66.82% of Python3 online submissions for Single Number II.
