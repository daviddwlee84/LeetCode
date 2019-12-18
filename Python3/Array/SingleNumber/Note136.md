# 136. Single Number

## Description

Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.

**Note**:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1**:

```txt
Input: [2,2,1]
Output: 1
```

**Example 2**:

```txt
Input: [4,1,2,1,2]
Output: 4
```

## Solution

### Hash Table

## Others' Solution

* [Official Solution](https://leetcode.com/problems/single-number/solution/)
  * List Operation: append and pop from a list
  * Hash Table: improve the list with a hash table
  * Math: use set to find unique numbers and double them then substract the sum
  * Bit Manipulation: A number XOR 0 is itself. And a number XOR itself is 0.
