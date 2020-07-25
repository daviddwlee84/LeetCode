from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        William's answer
        """
        candidate_set = set()  # all possible values you can get
        ans = float('inf')
        for num in arr:
            new_set = set([num])
            for item in candidate_set:
                new_set.add(num & item)
            for item in new_set:
                ans = min(ans, abs(item - target))
            candidate_set = new_set
        return ans
