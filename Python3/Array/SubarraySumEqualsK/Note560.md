# 560. Subarray Sum Equals K

## Description

Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.

**Example 1**:

```txt
Input:nums = [1,1,1], k = 2
Output: 2
```

**Note**:

1. The length of the array is in range [1, 20,000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integer **k** is [-1e7, 1e7].

> Hint:
>
> 1. Will Brute force work here? Try to optimize it.
> 2. Can we optimize it by using some extra space?
> 3. What about storing sum frequencies in a hash table? Will it be useful?
> 4. sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

## Solution

## Others' Solution

* [Official Solution](https://leetcode.com/problems/subarray-sum-equals-k/solution/)
