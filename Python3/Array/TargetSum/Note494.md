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

## Others' Solution

> [Target Sum Solution - LeetCode](https://leetcode.com/problems/target-sum/solution/)

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

* [**DP IS EASY! 5 Steps to Think Through DP Questions. - LeetCode Discuss**](https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.)
