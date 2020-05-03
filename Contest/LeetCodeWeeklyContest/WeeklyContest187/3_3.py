from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque() # [largest ... smallest]
        minDeque = deque() # [smallest ... largest]

        result = 1
        left = 0

        # find each longest subarray for every right pointer by shrinking left pointer
        for right in range(len(nums)):
            # update maxDeque with new right pointer
            while maxDeque and maxDeque[-1] < nums[right]:
                # if the current number is even smaller than the smallest max, 
                maxDeque.pop()
            maxDeque.append(nums[right])

            # update minDeque with new right pointer
            while minDeque and minDeque[-1] > nums[right]:
                minDeque.pop()
            minDeque.append(nums[right])

            # shrink left pointer if exceed limit
            while abs(maxDeque[0] - minDeque[0]) > limit:
                if maxDeque[0] == nums[left]:
                    maxDeque.popleft()
                if minDeque[0] == nums[left]:
                    minDeque.popleft()
                left += 1 # shrink it
            
            result = max(result, right - left + 1)
    
        return result

# Runtime: 408 ms, faster than 80.00% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
# Memory Usage: 24 MB, less than 100.00% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
