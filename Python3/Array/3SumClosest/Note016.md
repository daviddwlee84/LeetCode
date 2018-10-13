# 3Sum Closest

## Description

Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example**:

```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

## Solution

### Brute Force

* Time Complexity: O(n³)

* Calculate all the sum of three (three layer loops)
* Find the closest with the target

### Two Pointer

* Time Complexity: O(n²)

* Like last problem, sort the array to reduce the time complexity of searching
* Use two pointer to find the closest sum
    * If current sum equal to target then return
    * If found the closer one then update
    * Compare current sum with the target to consider which pointer to move

### Others

```python
class Solution:
    def threeSumClosest(self, nums, target):
        res = []
        nums.sort()
        for i,num in enumerate (nums[0:-2]):
            l = i + 1
            r  = len(nums) - 1
            if nums[l] + nums[l + 1] + num > target:
                res.append(nums[l] + nums[l + 1] + num)
            elif nums[r] + nums[r - 1] + num < target:
                res.append(nums[r] + nums[r - 1] + num)
            else:
                while l < r:
                    res.append(nums[l] + nums[r] + num)
                    if nums[l] + nums[r] + num < target:
                        l += 1
                    elif nums[l] + nums[r] + num > target:
                        r -= 1
                    else:
                        return target
        res.sort(key=lambda x:abs(x-target))
        return res[0]
```