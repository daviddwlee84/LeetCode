# 494. Target Sum

## Description

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from `+` and `-` as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

**Example 1**:

```txt
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

**Note**:

1. The length of the given array is positive and will not exceed 20.
2. The sum of elements in the given array will not exceed 1000.
3. Your output answer is guaranteed to be fitted in a 32-bit integer.

## Solution

### Backtracking

#### DFS

### Dynamic Programming

#### 2D

* build a table for each position and sum
* map the -1000~1000 each sum
* iterate through each position/index to calculate the sum

Base case

* position 0 with +- `nums[0]`

Result

* position `len(nums)-1` sum with `S`

#### 1D

* the same dp array will be updated for every row traversed

## Others' Solution

> [Target Sum Solution - LeetCode](https://leetcode.com/problems/target-sum/solution/)

* [**DP IS EASY! 5 Steps to Think Through DP Questions. - LeetCode Discuss**](https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.) - Bottom up recurssive with memory (no given DP code)
* [Java DFS & Memorization with Explanations - LeetCode Discuss](https://leetcode.com/problems/target-sum/discuss/169648/Java-DFS-and-Memorization-with-Explanations)

```java
private static Map<String, Integer> memo; // key: serialized curIndex and targetSum, value: its corresponding number of ways

public int findTargetSumWays(int[] nums, int S) {
    memo = new HashMap<>();
    return findTargetSumWaysRecur(nums, S, 0, S);
}

private static int findTargetSumWaysRecur(int[] nums, int S, int curIndex, int targetSum) {

    String curSerial= serialize(curIndex, targetSum);
    if (memo.containsKey(curSerial)) {
        return memo.get(curSerial);
    }

    if (curIndex == nums.length) {
        if (targetSum == 0) {
            return 1;
        }
        return 0;
    }

    int numWaysIfMinus = findTargetSumWaysRecur(nums, S, curIndex + 1, targetSum + nums[curIndex]); // -nums[curIndex]
    int numWaysIfAdd = findTargetSumWaysRecur(nums, S, curIndex + 1, targetSum - nums[curIndex]); // +nums[curIndex]

    int numWays =  numWaysIfMinus + numWaysIfAdd;
    memo.put(curSerial, numWays);
    return numWays;
}

private static String serialize(int curIndex, int targetSum) {
    return curIndex + "," + targetSum;
}
```

```py
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        total = sum(nums)
        if total < S or (total+S)%2: return 0
        target = (total-S) // 2
        dp = [0] * (target+1)
        dp[0] = 1
        for n in nums:
            for s in range(target, n-1, -1):
                dp[s] += dp[s-n]
        return dp[-1]
```

```py
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums.sort()

        slist = [0] * len(nums)
        slist[0] = nums[0]
        for i in range(1,len(nums)):
            slist[i] += nums[i] + slist[i - 1]

        s = slist[-1] + S

        if slist[-1] < S or s % 2: return 0

        s = s // 2

        dp = [1] + [0]*s
        for i, x in enumerate(nums):
            for m in range(min(s, slist[i]), x-1, -1):
                dp[m] += dp[m-x]
        return dp[-1]
```
