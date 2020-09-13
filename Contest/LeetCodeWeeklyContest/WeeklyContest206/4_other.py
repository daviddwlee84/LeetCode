from collections import deque


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        Alex Wice's Solution

        Insight: we can transform the question of sorted in length 2 => i.e. swap

        => that is Bubble Sort
        """
        index = [deque() for _ in range(10)]
        for i, x in enumerate(map(int, s)):
            index[x].append(i)

        # For example, with
        # s = "12313"
        # index[1] = deque([0, 3])
        # index[2] = deque([1])
        # index[3] = deque([2, 4])

        for x in map(int, t):
            if not index[x]:
                return False

            i = index[x].popleft()
            for lower in range(x):
                # if there is any "lower value" between i
                # then we "can't bubble sort through those values"
                # thus we may fail
                if index[lower] and index[lower][0] < i:
                    return False

        return True
