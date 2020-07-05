from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/discuss/720130/C%2B%2BJava%3A-two-way-street

        If two ants bump into each other and change directions, it's the same as if these ants continue as nothing happens.
        So, we can think about that plank as a two-way street. So, find the maximum units that any ant needs to travel.

        https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/discuss/720115/Python3-1-line-(brain-teaser)
        """
        # return max(max(left or [0]), n - min(right or [n]), 0)
        return max(max(left, default=0), n - min(right, default=n))
