# 315. Count of Smaller Numbers After Self

## Description

## Solution

## Others' Solution

* [计算右侧小于当前元素的个数 - 计算右侧小于当前元素的个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/)
* [归并排序计算逆序对 + 索引数组（Java、Python） - 计算右侧小于当前元素的个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/gui-bing-pai-xu-suo-yin-shu-zu-python-dai-ma-java-/)

---

## Fail

```py
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller_count = []
        _less_equal_count = []
        for i in reversed(range(len(nums))):
            # Find the first less than
            found = False
            less_equal_idx = None
            for j in range(i + 1, len(nums)):
                if less_equal_idx is None and nums[i] >= nums[j]:
                    less_equal_idx = j
                if nums[i] > nums[j]:
                    found = True
                    break

            if less_equal_idx is not None:
                _less_equal_count.append(
                    _less_equal_count[len(nums) - less_equal_idx - 1] + 1)
            else:
                _less_equal_count.append(0)

            if found:
                smaller_count.append(_less_equal_count[len(nums) - j - 1] + 1)
            else:
                smaller_count.append(0)

        return reversed(smaller_count)
```

* Fail when case like `[2, 0, 1]`, we can't just find a less equal then
