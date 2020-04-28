# First Unique Number

## Description

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the `FirstUnique` class:

* `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.
* `int showFirstUnique()` returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
* `void add(int value)` insert value to the queue.

**Example 1**:

```txt
Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
```

**Example 2**:

```txt
Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]

Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
```

**Example 3**:

```txt
Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1
```

**Constraints**:

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^8`
* `1 <= value <= 10^8`
* At most `50000` calls will be made to `showFirstUnique` and `add`.

## Solution

## Others' Solution

* [First Unique Number (LeetCode Day 28) - YouTube](https://www.youtube.com/watch?v=_y0FiPJXgZk)]

```py
from collections import Counter, deque

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.c = Counter(nums)
        self.d = deque(nums)

    def showFirstUnique(self) -> int:
        while self.d and self.c[self.d[0]] != 1:
            self.d.popleft()
        return self.d[0] if self.d else -1

    def add(self, value: int) -> None:
        self.c[value] += 1
        self.d.append(value)
```

```py
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = collections.OrderedDict()
        for num in nums:
            self.d[num] = self.d.get(num, 0) + 1
        self.removed = set()
        for key in list(self.d.keys()):
            if self.d[key] > 1:
                self.removed.add(key)
                self.d.pop(key)

    def showFirstUnique(self) -> int:
        return next(iter(self.d)) if self.d else -1

    def add(self, value: int) -> None:
        if value not in self.removed:
            if value in self.d:
                self.d.pop(value)
                self.removed.add(value)
            else:
                self.d[value] = 1
```
