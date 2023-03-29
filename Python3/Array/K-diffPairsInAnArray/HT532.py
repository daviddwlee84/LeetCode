from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        if k == 0:
            return sum(count >= 2 for count in counter.values())
        else:
            return sum(num + k in counter for num in counter.keys())


# Runtime: 76 ms, faster than 98.74% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.5 MB, less than 37.53% of Python3 online submissions for K-diff Pairs in an Array.

# similar with https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100135/JavaPython-Easy-Understood-Solution
