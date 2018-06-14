# 1. Two Sum

## Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Solution

### Naive

#### Complexity

* Time Complexity: O(nlogn)
* Space Complexity: O(1)

### Hesh Table

* Time Complexity: O(n)
* Space Complexity: O(n)

* Store the index of each value in the array
* Because it would have exactly one solution, so there must be a corresponding value in hash table

### Sorted Hesh Table

* Time Complexity: O(n)
* Space Complexity: O(n)

* Store the index of each value in the array
* Search from both sides of the back and beginning, and sum them to compare with target value