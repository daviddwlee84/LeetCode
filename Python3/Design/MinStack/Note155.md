# 155. Min Stack

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

**Example**:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

## Solution

* Key is how to return min with O(1) time.

### Naive

* Time Complexity
    * push - O(1)
    * pop - O(1)
    * top - O(1)
    * getMin - O(n)

### Improve

* Time Complexity
    * push - O(1)
    * pop - O(1)
    * top - O(1)
    * getMin - O(1)

### Others

* Push new number as a tuple (number, current min) (current min i.e. min(number, last min))

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
```

* If find new min, push last min into stack. Refresh min then push new number as normal.
* When the popped number is min, pop another number as new min which we pushed when we found this new min.

```python
class MinStack:
    def __init__(self):
        self.min = 2147483647
        self.stack = []

    def push(self, x):
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        peak = self.stack.pop()
        if peak == self.min:
            self.min = self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min
```

* Use another stack to store tuple of the newest found min (number, length of stack)
* So when popping element, if the min is at the top (i.e. length of stack == current length of stack), then pop from min stack as well.

```python
class MinStack:
    def __init__(self):
        self.S = []
        self.minS = []

    def push(self, x):
        if len(self.minS)==0 or x < self.minS[-1][0]:
            self.minS.append((x, len(self.S)))
        self.S.append(x)

    def pop(self):
        if len(self.S)==0:
            return None
        if len(self.S)-1==self.minS[-1][1]:
            self.minS.pop()
        return self.S.pop()

    def top(self):
        if len(self.S)==0:
            return None
        else:
            return self.S[-1]

    def getMin(self):
        if len(self.S)==0:
            return None
        else:
            return self.minS[-1][0]
```

* [Python Collections - Counter](https://docs.python.org/3.6/library/collections.html#collections.Counter)
* Use another min stack as the last example.
* Use Counter to maintain whether it need to pop from min stack (if that number is 0 (i.e. no longer in the stack))


```python
class MinStack:
    def __init__(self):
        self.stack = []
        from collections import Counter
        self.counts = Counter()
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        self.counts[x] += 1
        if not self.min_stack or self.min_stack[-1] > x:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        self.counts[self.stack[-1]] -= 1
        if self.counts[self.min_stack[-1]] == 0:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
```