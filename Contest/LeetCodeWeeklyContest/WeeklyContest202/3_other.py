from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Alex Wice's Solution

        intuition is tricky (but actually it's a common trick)
        answer is "binary search" for the answer (not intuitive)
        (like koko eats banana)

        try to put a ball "a" apart, and see if success or fail

        possible(force) on [0, 1, ..., max(positions)]
        [True, True, .., True, False, ...]
        We want "last true"
        """
        def possible(force: int):
            """
            How many balls can we place so that each pair
            of balls is >= `force` away from each other?
            """
            balls_placed = 0
            prev = float('-inf')  # most recent ball placed
            for x in position:
                if x - prev < force:
                    # not allowed to place ball here
                    continue

                # otherwise, place a ball
                prev = x
                balls_placed += 1

            return balls_placed >= m

        position.sort()

        # Binary search template to
        # Find the "last True" (maximum `force`) in map(possible, [0, 1, ..., max(positions)])

        low = 0
        high = position[-1]

        while low < high:
            mid = low + high + 1 >> 1
            if possible(mid):
                low = mid
            else:
                high = mid - 1

        return low
