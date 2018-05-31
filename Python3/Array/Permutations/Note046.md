# 46. Permutations

## Description

Given a collection of distinct integers, return all possible permutations.

**Example**:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Example

### Official [itertools](https://docs.python.org/3/library/itertools.html#itertools.permutations) Library

```python
import itertools
itertools.permutations([...])
```

### Others

[Pale Blue Dot](http://xiaohuiliucuriosity.blogspot.com/2014/12/permutations.html)

## Note

[How to clone or copy a list](https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list)

## Solution

* Time Complexity: all are O(n!)
  * [Why Time complexity of permutation function is O(n!)](https://stackoverflow.com/questions/39125471/why-time-complexity-of-permutation-function-is-on/39126141)
  * [Stirling's approximation](https://www.wikiwand.com/en/Stirling's_approximation)
  * [A Comparative Study on the Performance of Permutation Algorithms](http://www.lacsc.org/papers/Paper20.pdf)


### Backtracking

1. Each time add new number in nums into permuteTemp (check if the number is in permuteTemp)
2. If the length of permuteTemp is same as nums that is on of the answer

Summary

* nums: the total number collection
* permuteTemp: the temperary list

### Recursive

Basic idea: permutation of A[1..n] equals to
A[1] + permutation of (A[1..n] - A[1])
A[2] + permutation of (A[1..n] - A[2])
...
A[n] + permutation of (A[1..n] - A[n]).


### DFS-based

1. Each time pick an number from nums add to path and remove from nums
2. When no more number in nums that is one of the answer

Summary

* nums: the number haven't been used
* path: the temperary list