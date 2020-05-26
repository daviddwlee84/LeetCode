from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # count is used to store the relative number of ones and zeros
        # encountered so far while traversing the array
        # because count can range between -n ~ n
        # we need to make the array of size 2n + 1 to keep track of count
        # -2 means empty
        # -1 means 0 == 1
        # other number means current position

        array = [-2] * (2 * len(nums) + 1)
        array[len(nums)] = -1

        maxlen = 0
        count = 0

        for i in range(len(nums)):
            count = count + 1 if nums[i] == 1 else count - 1

            if array[count + len(nums)] >= -1:
                maxlen = max(maxlen, i - array[count + len(nums)])
            else:
                array[count + len(nums)] = i

        return maxlen


# Runtime: 1036 ms, faster than 8.84 % of Python3 online submissions for Contiguous Array.
# Memory Usage: 16.3 MB, less than 100.00 % of Python3 online submissions for Contiguous Array.
