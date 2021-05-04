# Non-Decreasing Array

## Description

## Solution

---

## Fail

This can't handle "first" case

```py
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        # diffs = []
        chance = True
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff < 0:
                if chance:
                    nums[i] = nums[i-1]
                    chance = False
                    # diff = 0
                else:
                    return False
            # diffs.append(diff)
        return True
```
