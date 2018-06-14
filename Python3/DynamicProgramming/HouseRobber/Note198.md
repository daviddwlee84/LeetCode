# 198. House Robber

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

**Example 1**:

```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Example 2**:

```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

## Solution

### Dynamic Programming

* Time Complexity: O(n)
* Space Complexity: O(n)

* Dynamic Programming Formula:
    * dp[0] = nums[0]
    * dp[1] = max(nums[0], nums[1])
    * dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

#### Save Space DP

* Space Complexity: O(1)

* Maintain two variable, and update them during odd and even turn respectively.

[example](http://www.cnblogs.com/grandyang/p/4383632.html)