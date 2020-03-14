# 253. Meeting Rooms II

## Description

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` (`si` < `ei`), find the minimum number of conference rooms required.

**Example 1**:

```txt
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2
```

**Example 2**:

```txt
Input: [[7, 10], [2, 4]]
Output: 1
```

## Solution

### Priority Queue (Min Heap)

1. Sort the intervals
2. Use priority queue to handle the minimal end time

Idea

* If the minimal end time is earlier than current start time, then we can put them in the same room => pop one out
* The size of the priority queue in the end will be the minimal room we need

## Notes

### Priority Queue in Python

* [Introduction to Priority Queues in Python - Towards Data Science](https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3)
  * `import heapq`
  * `from queue import PriorityQueue`