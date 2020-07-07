# 264. Ugly Number II

## Description

Write a program to find the `n`-th ugly number.

Ugly numbers are **positive numbers** whose prime factors only include `2, 3, 5`.

**Example**:

```txt
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```

**Note**:  

1. 1 is typically treated as an ugly number.
2. n **does not exceed 1690**.

## Solution

### Priority Queue

## Others' Solution

```py
class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]
```

## Interview

> Microsoft interview:
>
> 給一組質因數 例如 [2, 3, 5, 7] 然後要找出第n個任何一個的倍數，例如 [2, 3, 5] 然後要找第6個，那要return 8 因為符合的有 [2, 3, 4, 5, 6, 8]。
