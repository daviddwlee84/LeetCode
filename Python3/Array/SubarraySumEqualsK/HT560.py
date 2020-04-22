from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        If the cumulative sum upto two indices is the same,
        the sum of the elements lying in between those indices is zero

        =>

        If the cumulative sum upto two indices, say i and j is at a difference of k
        i.e. if sum[i] - sum[j] = k,
        the sum of elements lying between indices i and j is k.

        Time Complexity: O(n)
        Space Compleity: O(n)
        """

        # store the cumulative sum upto all the indices possible along with the number of times the same sum occurs
        hashmap = defaultdict(int)  # {sum_i: # of occurences of sum_i}

        count = 0
        s = 0
        hashmap[0] += 1

        for i in range(len(nums)):
            s += nums[i]
            count += hashmap[s - k]
            hashmap[s] += 1

        return count
