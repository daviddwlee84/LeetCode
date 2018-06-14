# 26. Remove Duplicates from Sorted Array

## Description

Given a sorted array nums, remove the duplicates [in-place](https://www.wikiwand.com/en/In-place_algorithm) such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array** [in-place](https://www.wikiwand.com/en/In-place_algorithm) with O(1) extra memory.

**Example 1**:

```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 2**:

```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

**Clarification**:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference**, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## Solution

### Naive

* Time Complexity: O(n)
* Space Commplexity: O(1) => in-place algorithm

1. Find the duplicated number (occur more than once), replace it to None
2. Remove all the None element in list
3. Calculate the lenth of list and return

### Better

1. Find the next different number
2. Use it to replace the number of the pointer index value
3. Cut the rest of the element in list (Optional)

### Other similar approach

```python
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = None
        pointer = 0
        for i in nums:
            if current != i:
                nums[pointer] = i
                current = i
                pointer += 1
        return pointer
```
