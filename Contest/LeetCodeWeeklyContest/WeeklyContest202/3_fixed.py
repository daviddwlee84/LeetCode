from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        https://www.geeksforgeeks.org/place-k-elements-such-that-minimum-distance-is-maximized/
        """
        n = len(position)

        def isFeasible(mid: int):
            pos = position[0]

            elements = 1

            # Try placing m elements with minimum distance mid
            for i in range(1, n):
                if position[i] - pos >= mid:
                    pos = position[i]
                    elements += 1

                    if elements == m:
                        return True

            return False

        position.sort()

        result = -1

        left = 0
        right = position[n - 1]

        while left < right:
            mid = (left + right) // 2

            if isFeasible(mid):
                result = max(result, mid)
                left = mid + 1
            else:
                right = mid

        return result

# WA
#
# [79,74,57,22]
# 4
#
# 5
#
#
# [20,73,90,55,21,52,26,46,57,51,95,13,30,68,32,15,31,44,23,82,17,33,12]
# 12
#
# 5
