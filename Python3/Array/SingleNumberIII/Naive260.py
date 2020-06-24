from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = set()
        for num in nums:
            if num in answer:
                answer.remove(num)
            else:
                answer.add(num)

        return list(answer)

# Runtime: 56 ms, faster than 88.47% of Python3 online submissions for Single Number III.
# Memory Usage: 15.7 MB, less than 11.45% of Python3 online submissions for Single Number III.
