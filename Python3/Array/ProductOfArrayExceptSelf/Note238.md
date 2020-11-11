# 238. Product of Array Except Self

## Description

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

**Example**:

```txt
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

**Constraint**: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

**Note**: Please solve it **without division** and in O(n).

**Follow up**:

Could you solve it with constant space complexity? (The output array **does not** count as extra space for the purpose of space complexity analysis.)

## Solution

## Others' Solution

* [Official Solution](https://leetcode.com/problems/product-of-array-except-self/solution/)

### Left and Right product lists

### Use output as a product list

> we will be using the output array as one of L or R and we will be constructing the other one on the fly
