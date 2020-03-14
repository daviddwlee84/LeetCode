# Maximum Number of Events That Can Be Attended

## Description

Given an array of `events` where `events[i] = [startDayi, endDayi]`. Every event `i` starts at `startDayi` and ends at `endDayi`.

You can attend an event `i` at any day `d` where `startTimei <= d <= endTimei`. Notice that you can only attend one event at any time `d`.

Return *the maximum number of events* you can attend.

**Example 1**:

![example 1](https://assets.leetcode.com/uploads/2020/02/05/e1.png)

```txt
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
```

**Example 2**:

```txt
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
```

**Example 3**:

```txt
Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
```

**Example 4**:

```txt
Input: events = [[1,100000]]
Output: 1
```

**Example 5**:

```txt
Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
```

**Constraints**:

* `1 <= events.length <= 10^5`
* `events[i].length == 2`
* `1 <= events[i][0] <= events[i][1] <= 10^5`

## Solution

### Greedy with Min Heap

> Similar with *scheduling meetings with limimted meeting rooms*

* Algorithm - Greedy: To always choose the event that ends sooner
* Data structure - Min Heap: To efficiently keep track of the biggest value (while you can dynamically add and remove elements) => sort the currently available events according to the ending day of the events

## Others' Solution

* [**【Detailed analysis】Let me lead you to the solution step by step - LeetCode Discuss**](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510262/Detailed-analysisLet-me-lead-you-to-the-solution-step-by-step)

Priority Queue

```py
class Solution(object):
    def maxEvents(self, events):
        events = [[s, e+1] for s, e in events]
        M = max(e for s,e in events)
        A = [[] for _ in xrange(M+1)]
        for s, e in events:
            A[s].append(e)

        pq = []
        ans = 0
        for d in range(1, M + 1):
            for e in A[d]:
                heapq.heappush(pq, e)
            while pq and pq[0] < d + 1:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1
        return ans
```

* [[Java/C++/Python] Priority Queue - LeetCode Discuss](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue)

```py
def maxEvents(self, A):
    A.sort(reverse=1)
    h = []
    res = d = 0
    while A or h:
        if not h: d = A[-1][0]
        while A and A[-1][0] <= d:
            heapq.heappush(h, A.pop()[1])
        res += 1
        d += 1
        while h and h[0] < d:
            heapq.heappop(h)
    return res
```

> ## Deprecated
>
> ```py
> from typing import List, Set
>
>
> class Solution:
>     def maxEvents(self, events: List[List[int]]) -> int:
>         if not events:
>             return 0
>
>         schedule = [set() for _ in range(int(1e5))]
>         maxEndDay = 0
>
>         for eventIdx, (startDay, endDay) in enumerate(events):
>             if endDay > maxEndDay:
>                 maxEndDay = endDay
>             for day in range(startDay-1, endDay):
>                 schedule[day].add(eventIdx)
>
>         schedule = schedule[:maxEndDay]
>
>         return self.backtracking(0, schedule, set())
>
>     def backtracking(self, day: int, schedule: List[Set[int]], attendedEvents: Set[int]) -> int:
>         if day >= len(schedule):
>             return 0
>         maxCount = 0
>         for event in schedule[day]:
>             if event in attendedEvents:
>                 return self.backtracking(day + 1, schedule, attendedEvents)
>
>         for possEvent in schedule[day]:
>             attendedEvents.add(possEvent)
>             count = self.backtracking(
>                 day + 1, schedule, attendedEvents.copy()) + 1
>             if count > maxCount:
>                 maxCount = count
>             attendedEvents.remove(possEvent)
>
>         return maxCount
>
>
> # Testcase
> # [[1, 2], [1, 3], [3, 4], [1, 2]], 3
> # [[1, 2], [2, 3], [3, 4], [1, 2]], 4
> ```
