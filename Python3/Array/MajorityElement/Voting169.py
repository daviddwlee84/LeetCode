from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if count == 0:
                # we effectively forget about everything in nums up to the current index
                # and consider the current number as the candidate for majority element
                candidate = num

            # count incremented whenever we see an instance of current candidate for majority element
            #       decremented whenever we see anything else
            count += (1 if num == candidate else -1)

        return candidate

# Runtime: 184 ms, faster than 40.41% of Python3 online submissions for Majority Element.
# Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.
