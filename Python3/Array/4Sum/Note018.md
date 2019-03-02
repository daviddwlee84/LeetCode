# 4Sum

> Similar with `3Sum` (a kind of a generalization)

## Description

Given an array `nums` of *n* integers and an integer `target`, are there elements *a, b, c*, and *d* in nums such that *a + b + c + d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Note**:

The solution set must not contain duplicate quadruplets.

**Example**:

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## Solution

### Generalized Two Pointer

[Python 140ms beats 100%, and works for N-sum (N>=2)](https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2))

Key point:

* Reduce the problem into 2Sum.
* Use two pointer to make sure not duplicate
* Sort the array first
