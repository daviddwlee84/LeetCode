# 55. Jump Game

## Description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

**Example 1**:

```txt
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2**:

```txt
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

## Solution

## Others' Solution

* [Official Solution](https://leetcode.com/problems/jump-game/solution/)

This is a dynamic programming question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:

1. Start with the recursive backtracking solution
2. Optimize by using a memoization table (top-down dynamic programming)
3. Remove the need for recursion (bottom-up dynamic programming)
4. Apply final tricks to reduce the time / memory complexity

### Backtracking

### Dynamic Programming Top-down

### Dynamic Programming Bottom-up

### Greedy

---

Fail draft

```py
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        greedy
        """
        i = 0
        temp_max = 0
        while i < len(nums) - 1:
            import ipdb; ipdb.set_trace()
            for j in range(nums[i]):
                if i + j > len(nums) - 1:
                    break
                temp_max = max(i + nums[i + j], temp_max)

            if temp_max == i:
                return False

            i = temp_max

        return True
```
