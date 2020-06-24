from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/single-number-ii/discuss/699889/Python-Bit-Manipulation-O(32n)-but-easy-exaplained

        count each bit module 3
        """

        # for each bit can have either 0 or 1 and never 2
        single = 0

        # iterate over all possible 32 bits
        for i in range(32):
            count = 0

            # for each num check if this num has non-zero bit on position i
            for num in nums:
                if num & (1 << i) == (1 << i):
                    count += 1

            # evaluate this sum module 3
            single |= (count % 3) << i

        # deal with overflow cases
        # (maximum value for int32 is 2**31-1, if we get number more than this, we have negative answer)
        return single if single < (1 << 31) else single - (1 << 32)

# Runtime: 136 ms, faster than 13.36% of Python3 online submissions for Single Number II.
# Memory Usage: 15.5 MB, less than 55.04% of Python3 online submissions for Single Number II.
