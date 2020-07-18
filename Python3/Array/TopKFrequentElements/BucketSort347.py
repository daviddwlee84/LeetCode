from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/discuss/81602/Java-O(n)-Solution-Bucket-Sort
        """
        count = Counter(nums)
        bucket = [None] * (len(nums) + 1)

        for num, frequency in count.items():
            if bucket[frequency] is None:
                bucket[frequency] = []
            bucket[frequency].append(num)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] is not None:
                result.extend(bucket[i])

            if len(result) >= k:
                break

        # It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
        # otherwise we should return result[:k]
        return result

# Runtime: 108 ms, faster than 71.17% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.3 MB, less than 62.04% of Python3 online submissions for Top K Frequent Elements.
