# Next Permutation

## Description

Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

`1,2,3` → `1,3,2`
`3,2,1` → `1,2,3`
`1,1,5` → `1,5,1`

## Solution

### Naive

* Find all the permutation
* Compare with the input

> TODO: Understand permutation with duplicates

### Single Pass Approach

1. Find first decreasing element from the end of the array
   * peak as *i*
   * the element as *i-1*
2. Find number just right larger than nums[i-1]
3. Swap these two numbers
4. Reverse the element from *i* to the end (include *i*)

* Time complexity: O(n)
* Space complexity: O(1)

#### Others

```py
class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i, j = n-1, n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i == 0:
            nums[:]=nums[::-1]
            return

        for j in range(n-1, i-2, -1):
            if nums[j] > nums[i-1]:
                break

        nums[j], nums[i-1] = nums[i-1], nums[j]
        nums[i:] = nums[i:][::-1]
```

## Links

* [Computing permutations with duplicates (Python recipe)](https://code.activestate.com/recipes/496869-computing-permutations-with-duplicates/)
