# 658. Find K Closest Elements

## Description

## Solution

---

## Fail

Not simply near the center

```py
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        https://docs.python.org/3/library/bisect.html
        """
        index = bisect.bisect_left(arr, x)

        # print(index)

        left = index - (k + (arr[index] != x)) // 2
        right = index + (k + (arr[index] == x)) // 2
        if left < 0:
            right += 0 - left
            left = 0
        elif right > len(arr):
            left -= right - len(arr)
            right = len(arr)
        return arr[left:right]
```
