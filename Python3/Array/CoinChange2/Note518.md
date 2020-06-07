# 518. Coin Change 2

## Description

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

**Example 1**:

```txt
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2**:

```txt
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3**:

```txt
Input: amount = 10, coins = [10]
Output: 1
```

**Note**:

You can assume that

* 0 <= amount <= 5000
* 1 <= coin <= 5000
* the number of coins is less than 500
* the answer is guaranteed to fit into signed 32-bit integer

## Solution

## Others' Solution

* [100% Faster | Recursive, 1-d, 2-d DP | Matrix With Example | Commented Code Video - LeetCode Discuss](https://leetcode.com/problems/coin-change-2/discuss/674977/100-Faster-or-Recursive-1-d-2-d-DP-or-Matrix-With-Example-or-Commented-Code-Video)
* [[Python] 2 Lines Magical solution with Generating functions - LeetCode Discuss](https://leetcode.com/problems/coin-change-2/discuss/675424/Python-2-Lines-Magical-solution-with-Generating-functions)

```py
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        C = [0] * (amount + 1)
        C[0] = 1

        for d in coins:
            for i in range(d, amount + 1):
                C[i] += C[i-d]
        return C[amount]
```

```py
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount)
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
```
