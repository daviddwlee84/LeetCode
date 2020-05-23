# 986. Interval List Intersections

## Description

Given two lists of **closed** intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

*(Formally, a closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)*

**Example 1**:

```txt
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
```

**Note**:

1. `0 <= A.length < 1000`
2. `0 <= B.length < 1000`
3. `0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9`

**NOTE**: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## Solution

## Others' Solution

* [Official](https://leetcode.com/problems/interval-list-intersections/solution/)

Concate and Merge overlap (144ms)

```py
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        together = A + B
        together.sort()

        pos, cur_start, cur_end = 1, together[0][0], together[0][1]
        res = []
        while pos < len(together):
            if together[pos][0] > cur_end:
                cur_start, cur_end = together[pos]
            else:
                res.append((together[pos][0], min(cur_end, together[pos][1])))
                if together[pos][1] > cur_end:
                    cur_start, cur_end = together[pos]
            pos += 1
        return res
```

--

## Fail

```py
from typing import List
import numpy as np


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        A_binary = 0
        B_binary = 0
        for start, end in A:
            for i in range(start, end + 1):
                A_binary |= 1 << i
            print(bin(A_binary))

        for start, end in B:
            for i in range(start, end + 1):
                B_binary |= 1 << i
            print(bin(B_binary))

        prev = None
        start = None
        answer = []

        print(A, B, bin(A_binary), bin(B_binary), bin(A_binary & B_binary))
        for i, char in enumerate(reversed(bin(A_binary & B_binary)[2:])):
            if prev is not None:
                if prev == '1':
                    if char == '0':
                        answer.append([start, i - 1])
                        start = None
                else:
                    if char == '1':
                        start = i
            prev = char

        if start is not None:
            answer.append([start, i])

        return answer


if __name__ == "__main__":
    print(Solution().intervalIntersection([[0, 2], [5, 10], [13, 23], [
        24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
```
