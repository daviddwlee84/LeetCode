from typing import List
from collections import Counter
from bisect import bisect_left, bisect_right
# binary search
# https://docs.python.org/3/library/bisect.html


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/3sum/discuss/724777/Python-or-Beats-99-or-binary-search-or-no-two-pointer
        """
        # something like hash table with frequency (deal with duplicate)
        counter = Counter(nums)
        # this will get the sorted keys (i.e. non-duplicate numbers)
        nums = sorted(counter)

        result = []

        for i, num in enumerate(nums):
            # case 1: three numbers are the same i.e. [0, 0, 0]
            if num == 0:
                if counter[num] > 2:
                    result.append([0, 0, 0])

            # case 2: two numbers are the same
            # (else if is necessary)
            elif counter[num] > 1 and -2 * num in counter:
                result.append([num, num, -2 * num])

            # case 3: not any of the three numbers are the same
            if num < 0:
                target = -num

                # search the left most starting point, if not found then start from i + 1
                left = bisect_left(nums, target - nums[-1], i + 1)
                # search the right most starting point, if not found then start form left
                right = bisect_left(nums, target / 2, left)
                for a in nums[left:right]:
                    b = target - a
                    if b in counter and a != b:
                        result.append([num, a, b])

        return result

# Runtime: 224 ms, faster than 99.44% of Python3 online submissions for 3Sum.
# Memory Usage: 17.8 MB, less than 19.05% of Python3 online submissions for 3Sum.
