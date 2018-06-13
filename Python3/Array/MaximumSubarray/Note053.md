# 53. Maximum Subarray

## Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example**:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up**:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


## Solution

### Brute Force

(LeetCode: Time Limit Exceeded)

* Time Complexity: O(n³):
    * n: compare array length
    * n: start position
    * n: sum

### Dynamic Programming

* Time Complexity: O(n)
* Space Complexity: O(1)

* Reference: Kadane's Algorithm

* **DP Element** - current sum (status i): the max array sum when the ith element is the last element
* General Term Formula: current sum (status i) = current sum (status i-1) <= 0 ? ith element : current sum (status i-1) + ith element

Because current sum status i depend on status i-1, it only need one variable to store previous status.
(It's okay to use an array of length n to store each status, but space complexity will be O(n))

#### Procedure

1. Go through every element in array
2. Check if current sum > 0
    * if current sum > 0 => add next element
    * if current sum < 0 => replace with next element
3. Update max sum with current sum (if current sum is larger)

(Some Example / Explanation: [ex1](https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts), [ex2](http://theoryofprogramming.com/2016/10/21/dynamic-programming-kadanes-algorithm/))

### Divide and Conquer

* Time Complexity: O(nlogn)

* Reference: Introduction to Algorithm 3ed. Ch4-1

#### Procedure

1. Divide the given array in two halves
2. Return the maximum of following three
    1. Maximum subarray sum in left half (Make a recursive call)
    2. Maximum subarray sum in right half (Make a recursive call)
    3. Maximum subarray sum such that the subarray crosses the midpoint

(Some Example / Explanation: [ex1](https://www.geeksforgeeks.org/divide-and-conquer-maximum-sum-subarray/))