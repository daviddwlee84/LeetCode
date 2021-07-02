from typing import List
from collections import deque
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary Search (insertion sort like), and then try to insert the closest items
        https://docs.python.org/3/library/bisect.html
        """
        if k == 0:
            return []

        index = bisect.bisect_left(arr, x)
        if index >= len(arr):
            index = len(arr) - 1

        # print(index, arr[index], x)

        if arr[index] == x:
            answer = deque([x])
            right = index + 1
        else:
            right = index
            answer = deque()
        left = index - 1

        while len(answer) < k:
            left_diff = abs(arr[left] - x) if left >= 0 else float('inf')
            right_diff = abs(
                arr[right] - x) if right < len(arr) else float('inf')
            # print(left_diff, right_diff)
            # print(answer)

            if left_diff < right_diff or left_diff == right_diff:
                answer.appendleft(arr[left])
                left -= 1
            else:
                answer.append(arr[right])
                right += 1

        return answer

# Runtime: 308 ms, faster than 52.20% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.6 MB, less than 40.37% of Python3 online submissions for Find K Closest Elements.
