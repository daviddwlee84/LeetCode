from typing import List
import bisect


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/kth-missing-positive-number/solutions/3262163/c-java-python3-1-line-o-logn/
        """
        # https://docs.python.org/3.10/library/bisect.html
        # Changed in version 3.10: Added the key parameter.
        return bisect.bisect_right(range(0, len(arr)), k, key=lambda x: arr[x] - x) + k
