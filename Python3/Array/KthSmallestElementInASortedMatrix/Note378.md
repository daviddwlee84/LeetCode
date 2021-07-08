# Kth Smallest Element in a Sorted Matrix

## Description

## Solution

---

## Fail

```py
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        k -= 1
        return matrix[k // len(matrix)][k % len(matrix)]
```

```py
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        We know the outer (top-left) will always be smaller than the bottom-right corner => (this is not true)
        
        (X) matrix[k // len(matrix)][k % len(matrix)]
        """

        m, n = len(matrix), len(matrix[0])
        count = 0
        
        layer = 0
        while True:
            next_count = (m - layer) + (n - layer) - 1
            # print(next_count)
            if count + next_count >= k:
                break
            count += next_count
            layer += 1
        print(count, layer)

        i = j = layer + 1
        count += 1  # the top-left corner one
        if count == k:
            return matrix[layer][layer]

        while k > count:
            if j > n - 1:
                if count + 1 == k:
                    return matrix[i][layer]
                print(matrix[i][layer])
                i += 1
            elif i > n - 1:
                if count + 1 == k:
                    return matrix[layer][j]
                print(matrix[layer][j])
                j += 1


            elif matrix[layer][j] < matrix[i][layer]:
                if count + 1 == k:
                    return matrix[layer][j]
                print(matrix[layer][j])
                j += 1
            else:
                if count + 1 == k:
                    return matrix[i][layer]
                print(matrix[i][layer])
                i += 1


            count += 1
```
                