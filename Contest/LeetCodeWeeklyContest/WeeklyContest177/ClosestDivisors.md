# Closest Divisors

## Description

Given an integer `num`, find the closest two integers in absolute difference whose product equals `num + 1` or `num + 2`.

Return the two integers in any order.

**Example 1**:

```txt
Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
```

**Example 2**:

```txt
Input: num = 123
Output: [5,25]
```

**Example 3**:

```txt
Input: num = 999
Output: [40,25]
```

## Solution

> Key: reduce the looping range

## Deprecated

```py
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num_1_candidate, diff_1 = self.getClosestDivisors(
            num + 1, float('inf'))
        num_2_candidate, diff_2 = self.getClosestDivisors(num + 2, diff_1)

        if diff_1 < diff_2:
            return num_1_candidate
        return num_2_candidate

    def getClosestDivisors(self, num: int, diff: float) -> List[int]:
        candidate = None

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                div = num // i
                if i <= div:
                    temp_diff = div - i
                    if temp_diff < diff:
                        diff = temp_diff
                        candidate = [i, div]
                else:
                    break

        return candidate, diff

    def getClosestDivisors2(self, num: int) -> List[int]:
        divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
        divisors.append(num)
        if len(divisors) % 2 == 0:
            return [divisors[len(divisors) // 2 - 1], divisors[len(divisors) // 2]], divisors[len(divisors) // 2] - divisors[len(divisors) // 2 - 1]
        else:
            return [divisors[len(divisors) // 2], divisors[len(divisors) // 2]], 0

# TLE for testcase 170967091, 532378497, 722900699
```
