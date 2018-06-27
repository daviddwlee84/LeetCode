# 78. Subsets

## Description

Given a set of **distinct** integers, nums, return all possible subsets (the power set).

**Note**: The solution set must not contain duplicate subsets.

**Example**:

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Solution

### Binary

* Time Complexity: O(2ⁿ)

1. Generate 2ⁿ binaries.
2. Use the binaries as the iterator. => If the corresponding position is 1 then pick that number

### DFS Based

* Time Complexity: O(2ⁿ)

1. Make a helper function to find whether the start position element need to be add
  1. If the start position reach the end => that's one of the answer
  2. Recursive call the function for the next start position
    1. With current start position element
    2. Without current start position elemen

### Backtracking


### Others

```python
class Solution:
    def subsets(self, nums):
        def dfs(depth, start, layerlist):
            res.append(layerlist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, layerlist+[nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res
```

## Resources

* [Print all subsets (power set) of a given set](https://coderbyte.com/algorithm/print-all-subsets-given-set)
* [3 ways to the powerset in Python](http://salvia.logdown.com/posts/249530-hello-world)