from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = 0
        count = 0
        hashmap = {0: -1}  # we can get i-(-1) => i + 1 when count = 0
        for i in range(len(nums)):
            count = count + 1 if nums[i] == 1 else count - 1

            if count in hashmap:
                maxlen = max(maxlen, i - hashmap[count])
            else:
                hashmap[count] = i

        return maxlen

# Runtime: 908 ms, faster than 66.92% of Python3 online submissions for Contiguous Array.
# Memory Usage: 18.3 MB, less than 16.67% of Python3 online submissions for Contiguous Array.
