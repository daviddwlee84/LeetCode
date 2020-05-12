from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        stack = set()
        for num in nums:
            if num in stack:
                stack.remove(num)
            else:
                stack.add(num)
        
        return stack.pop()

# Runtime: 80 ms, faster than 22.60% of Python3 online submissions for Single Element in a Sorted Array.
# Memory Usage: 16.1 MB, less than 7.69% of Python3 online submissions for Single Element in a Sorted Array.
