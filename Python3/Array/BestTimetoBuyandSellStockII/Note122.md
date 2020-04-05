# 122. Best Time to Buy and Sell Stock II

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note**: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1**:

```txt
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

**Example 2**:

```txt
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3**:

```txt
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solution

[Official Solution](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/)

### Brute Force

* Time Complexity: O(nⁿ)

Try all the possible transactions and find the maximum profit.
But it's obvious not a good solution.

(LeetCode: Time Limit Exceeded)

### Greedy (Peak Valley Approach)

* Time Complexity: O(n)

Collect peak (local maximum) and valley (local minimum) when go through the array.

1. Find the ith valley first (the next profit goes up)
2. Then find the ith peak (the next profit goes down)
3. Add profit to the sum

### Tricky

* Time Complexity: O(n) - Single pass
* Space Complexity: O(1)

Because it don't need any transaction fee, we can buy and sell many times we want.
So we can buy it every time and sell it the next day (if the price goes up), then we are able to find another stock and won't be restrict in the "may not engage in multiple transactions at the same time" condition.

## Others' Solution

* [LeetCode Challenge Day 5 - Buy and Sell Stock II - YouTube](https://www.youtube.com/watch?v=MTnFIF2I2gw)
