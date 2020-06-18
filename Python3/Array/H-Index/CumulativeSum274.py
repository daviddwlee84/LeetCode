from typing import List
from itertools import accumulate


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        https://leetcode.com/problems/h-index/discuss/656820/Python-O(n)-timeandspace-with-explanation
        https://stackoverflow.com/questions/15889131/how-to-find-the-cumulative-sum-of-numbers-in-a-list/15889203#15889203
        """
        N = len(citations)
        # number of paper with i citation
        buckets = [0] * (N + 1)

        for cite in citations:
            # if number of citations is more than total number of papers N,
            # we can reduce this numberr to N
            buckets[min(cite, N)] += 1

        cumulative_sum = list(
            reversed(list(accumulate(reversed(buckets[1:])))))
        compare = [cumulative_sum[i] >= i + 1 for i in range(N)]
        return (compare + [0]).index(0)  # find the first index == False
