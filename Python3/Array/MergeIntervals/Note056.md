# 56. Merge Intervals

## Description

Given a collection of intervals, merge all overlapping intervals.

**Example 1**:

```txt
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2**:

```txt
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE**: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## Solution

### Sorting

1. Sort the interval with start time
2. If end time of last interval is greater or equal current start time. Then they can be combined.
