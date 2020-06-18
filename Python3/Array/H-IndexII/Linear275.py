from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        https://leetcode.com/problems/h-index/discuss/693418/Java-or-Simple-one
        """

        N = len(citations)
        index = 0
        while index < N and N - index > citations[index]:
            index += 1

        return N - index
