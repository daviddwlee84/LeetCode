# 621. Task Scheduler

## Description

You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the **least** number of units of times that the CPU will take to finish all the given tasks.

**Example 1**:

```txt
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

**Example 2**:

```txt
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```

**Example 3**:

```txt
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

**Constraints**:

* The number of tasks is in the range `[1, 10000]`.
* The integer n is in the range `[0, 100]`.

## Solution

### Priority Queue

## Others' Solution

* [Python, Straightforward with Explanation - LeetCode Discuss](https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation)

```py
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count-1) * (n+1) + max_count_tasks)
```

```py
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        class Task(object):
            """
                Task class to encapsulate notion of task
            """
            def __init__(self, name, count):
                self.name  = name       # name of task
                self.count = -count     # number of instances
                self.time  = -1         # time at which it last ran

            def __repr__(self):
                return self.name +':' +str(self.count)

            def schedule(self, time):
                self.time   = time      # task is scheduled, update time at which it last ran
                self.count  += 1        # decrease count

            #def __cmp__(self, other):
            #    cmp(self.count, other.count)

            def __lt__(self, other):
                # if two have same count, use the one with lexicographically smaller
                return self.count < other.count or self.count == other.count and self.name < other.name

        if n == 0:
            # if no cooling period, simply return as many tasks as there're
            return len(tasks)



        task_collection = collections.Counter(tasks) # count task occurrences
        cpu_slots       = []                         # a sequence depicting which task runs when
        runq            = []                         # a run queue,  a priority queue
        waitq = collections.deque([])                # a wait queue, a simple queue

        # push all tasks in a run que
        for name, count in task_collection.items():
            heapq.heappush(runq, Task(name, count))  # higher the instances, higher the priority

        idle_task = Task("idle", 0) # an idle task
        time = 0                    # clock
        while runq or waitq:        # if at least one of the queue has some tasks to run

            if waitq and ( time - waitq[0].time ) > n:  # if wait queue has task whose cooling period has come
                heapq.heappush(runq,waitq.popleft())    # put that task in run queue

            if runq:     # schdule highest priority task, if one is ready
                task = heapq.heappop(runq)
                task.schedule(time)  # consume one instance
            else:       # no task is ready, so schedule idle task
                task = idle_task

            cpu_slots.append(task.name) # task scheduled on CPU
            if task is not idle_task and task.count != 0:
                waitq.append(task)      # if task is not idle task and has at least some instances to run
            time += 1

        return len(cpu_slots)   # cpu slots will also print task schedule
```
