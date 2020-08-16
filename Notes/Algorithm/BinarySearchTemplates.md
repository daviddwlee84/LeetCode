# Binary Search Templates and Common Trick

## Prevent from overflow when calculating mid

Overflow will occur when A + B is super big (in other language like C++).

```py
(A + B) // 2
```

```py
A + B >> 1
```

Solution

```py
A + (B - A) // 2
```

## Finding First and Last True in an Array

> [reference](https://youtu.be/PZn394-UK-E?t=850)

This is EXACTLY the `bisect_left` and `bisect_right` in [`bisect.py`](https://svn.python.org/projects/python/trunk/Lib/bisect.py)

### Find first True

```txt
[False, False, False, True, True, ...]
                       ^ to find this one
```

```py
A = [False, False, False, True, True]

lo, hi = 0, len(A)
while lo < hi:
    mi = lo + hi >> 1
    if not possible(mi):
        lo = mi + 1
    else:
        hi = mi
return lo  # if lo == len(A), not found
```

### Find last True

```txt
[True, True, True, True, False, ...]
                    ^ to find this one
```

```py
A = [True, True, True, True, False, False]

lo, hi = 0, len(A) - 1
while lo < hi:
    mi = lo + hi + 1 >> 1
    if possible(mi):
        lo = mi
    else:
        hi = mi - 1
    return lo  # if lo == -1, not found
```

Example:

* [Magnetic Force Between Two Balls - LeetCode Contest](https://leetcode.com/contest/weekly-contest-202/problems/magnetic-force-between-two-balls/)
  * [Place k elements such that minimum distance is maximized - GeeksforGeeks](https://www.geeksforgeeks.org/place-k-elements-such-that-minimum-distance-is-maximized/)
* [Koko Eating Bananas - LeetCode](https://leetcode.com/problems/koko-eating-bananas/)
