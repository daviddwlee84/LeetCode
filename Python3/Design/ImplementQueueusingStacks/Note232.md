# 232. Implement Queue using Stacks

## Description

Implement the following operations of a queue using stacks.

* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.

**Example**:

```cpp
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

**Notes**:

* You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## Solution

## Others' Solution

[Official Solution](https://leetcode.com/problems/implement-queue-using-stacks/solution/)

Approach 1: push O(n), pop O(1)

```py
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1
```

> Approach 2: push O(1), pop amortized O(1)

```py
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2
```
