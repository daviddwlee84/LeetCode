from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """
        Alex Wice's solution
        """
        def possible(k: int):
            """
            Is p a subsequence of s where removable[:k] indices are removed?
            """
            banned = set(removable[:k])
            j = 0  # we want to match p[j] currently

            for i, c in enumerate(s):
                if i in banned:
                    continue

                if c == p[j]:
                    j += 1
                    if j == len(p):
                        return True

        # Find the last True in a sequence of True to False
        # F F F F F "T" T T T T T
        low, high = 0, len(removable)
        while low < high:
            mid = low + high + 1 >> 1
            if possible(mid):
                low = mid
            else:
                high = mid - 1

        return low
