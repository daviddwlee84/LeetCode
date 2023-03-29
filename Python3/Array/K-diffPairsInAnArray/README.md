# 532. K-diff Pairs in an Array

## Description

Given an array of integers nums and an integer k, return *the number of **unique** k-diff pairs in the array*.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

* `0 <= i < j < nums.length`
* `|nums[i] - nums[j]| == k`

**Notice** that `|val|` denotes the absolute value of `val`.

**Example 1**:

```txt
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```

**Example 2**:

```txt
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

**Example 3**:

```txt
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

**Constraints**:

* `1 <= nums.length <= 104`
* `-107 <= nums[i] <= 107`
* `0 <= k <= 107`

## Solution

### Brute Force

Find all combination and count

### Hash Table

Count frequency of all numbers.

## Fail Solution

```py
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        target_minus = []
        target_plus = []
        for num in nums:
            target_minus.append(num - k)
            target_plus.append(num + k)

        # print(target_minus)
        # print(target_plus)

        pairs = 0
        for i, num in enumerate(nums):
            pairs += num in target_minus[i + 1:]
            if k == 0:
                continue
            pairs += num in target_plus[i + 1:]

            # pairs += target_minus[i + 1:].count(num)
            # pairs += target_plus[i + 1:].count(num)
            # pairs += sum(num == target for target in target_minus[i + 1:])
            # pairs += sum(num == target for target in target_plus[i + 1:])

        return pairs
```
