from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one_set = set()
        more_than_one = set()

        for num in nums:
            if num in more_than_one:
                continue

            if num in one_set:
                one_set.remove(num)
                more_than_one.add(num)
            else:
                one_set.add(num)

        return one_set.pop()

# Runtime: 48 ms, faster than 98.40% of Python3 online submissions for Single Number II.
# Memory Usage: 15.8 MB, less than 5.12% of Python3 online submissions for Single Number II.
