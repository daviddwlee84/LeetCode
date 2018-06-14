# 189. Rotate Array

## Description

Given an array, rotate the array to the right by k steps, where k is non-negative.

**Example 1**:

```
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2**:

```
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

**Note**:

* Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
* Could you do it in-place with O(1) extra space?

## Solution

[Official Solution](https://leetcode.com/problems/rotate-array/solution/)

### Naive In-place

* Time Complexity: O(k) (but somehow it take so much time)
* Space Complexity: O(1)

1. Just rotate: shift nums[0 ~ length-1] right and insert nums[length-1] to nums[0]

### Use an Extra Array

* Time Complexity: O(n)
* Space Complexity: O(n)

1. Calculate the rotaiton result directly.
    * nums[i] --> nums[(i+k) % length]
2. Assign the temp array to origin (by refference)
    * It will need a loop to pass each value

### Simplify In-place

* Time Complexity: O(1)
* Space Complexity: O(1)

Modulo in python will return positive value: e.g. -13 % 7 = 1 / -6 % 4 = 2

(Python can automatically maintain negative index.)
(And it seem like the test case won't exceed two times of length, but it doesn't matter.)
